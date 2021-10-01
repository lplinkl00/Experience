import random
import math
import matplotlib.pyplot as plt

class Particle:
  def __init__(self, position = 0, velocity = 0):
    self.position = position
    self.velocity = velocity
    self.best_position = position
    self.position_list = [position]
    self.velocity_list = [velocity]
    self.best_position_list = []
    
  def update_personal_best(self):
    # 1. calculate the fitnesses of the best_position and the particle's current position
    best_pos_fitness = fitnessfunc(self.best_position)
    current_pos_fitness = fitnessfunc(self.position)
    # 2. compare the fitnesses and determine if the current position is better than the best_position
    if current_pos_fitness < best_pos_fitness:
      # 3. update if necessary
      self.best_position = self.position
    # 4. no return statement is required
    self.best_position_list.append(self.best_position)

  def update_velocity(self, alpha, beta, glob_best_pos):
    self.velocity = 0.5*self.velocity + alpha[0] * beta[0] * (self.best_position - self.position) + alpha[1] * beta[1] * (glob_best_pos - self.position)
    # self.velocity = alpha[0] * beta[0] * (self.best_position - self.position) + alpha[1] * beta[1] * (glob_best_pos - self.position)
    self.velocity_list.append(self.velocity)

  def update_position(self, position_limits):
    self.position = self.position + self.velocity
    self.position = max(min(self.position, position_limits[1]), position_limits[0])
    self.position_list.append(self.position)

def fitnessfunc(position):
    fitness = math.ceil(position) * 30 + (7 - math.floor(position)) * 25 + movingprice(time2hourmin(position)[0],time2hourmin(position)[1]) + (1 - renolevel(position)) * 80
    return fitness

def renolevel(time):
    renovationlevel = time ** 2 / 126 + time / 63 + 0.5
    return renovationlevel

def convert2time(day, hour, minute):
    time = day - 1 + (60 * hour + minute) / (24 * 60)
    return time
    
def movingprice(hour,minute):
    t = hour + minute / 60
    price = 50 * math.cos(12 * math.pi * t / 24) + 50 * math.cos(8 * math.pi * t / 24) + 150
    return price

def time2hourmin(time):
    time = time % 1
    hour = math.trunc((time * 24))
    minute = math.ceil((time * 24) % 1 * 60)
    return hour, minute

def initialise_particles(n_ptc, position_limits):
  # position_limits is a list of two values. The first value is the lower boundary and the second value is the upper boundary.
  particles = [Particle(random.random() * (position_limits[1] - position_limits[0]) + position_limits[0]) for _ in range(n_ptc)]
  return particles

def compareFitness(pos1, pos2):
    fitness1 = fitnessfunc(pos1)
    fitness2 = fitnessfunc(pos2)
    if fitness1 < fitness2:
        betterpos = pos1
    else:
        betterpos = pos2
    return betterpos

def calc_avg_fit_diff(particles):
    # 1. calculate mean fitness of all particles
    avg_fit = sum([fitnessfunc(p.position) for p in particles]) / len(particles)
    # 2. calculate the difference between the mean fitness and the fitness of each particle
    fit_diff = [abs(fitnessfunc(p.position) - avg_fit) for p in particles]
    # 3. calculate the average of the differences obtained from step 2
    avg_fit_diff = sum(fit_diff) / len(particles)
    return avg_fit_diff

def calc_avg_pos_diff(particles):
    # 1. calculate mean position of all particles
    avg_pos = sum([p.position for p in particles]) / len(particles)
    # 2. calculate the difference between the mean position and the position of each particle
    pos_diff = [abs(p.position - avg_pos) for p in particles]
    # 3. calculate the average of the differences obtained from step 2
    avg_pos_diff = sum(pos_diff) / len(particles)
    return avg_pos_diff

if __name__ == '__main__':
  alpha = [0, 0.1]
  n_particle = 15
  global_best_position = None
  global_best_position_list = []
  position_limits = [0, 7]
  iteration = 0
  max_iter = 200
  min_avg_fit_diff = 0.1
  min_avg_pos_diff = 0.1
  # initialise particles
  particles = initialise_particles(n_particle, position_limits)
  space_ax = plt.axes()
  space_ax.plot(list(range(*position_limits)),[fitnessfunc(x) for x in range(*position_limits)])
  space_ax.set_title("Position of particles in iteration {}".format(iteration))
  space_ax.set_xlabel("Position")
  space_ax.set_ylabel("Fitness")
  while (iteration < max_iter and calc_avg_fit_diff(particles) > min_avg_fit_diff and calc_avg_pos_diff(particles) > min_avg_pos_diff): # how should you define the termination criteria here?
    print(iteration, [round(x.position,2) for x in particles])
    print(iteration, calc_avg_fit_diff(particles), calc_avg_pos_diff(particles))
    if len(space_ax.lines) > 1:
      del space_ax.lines[1]
    space_ax.plot([x.position for x in particles], [fitnessfunc(x.position) for x in particles], 'go')
    space_ax.set_title("Position of particles in iteration {}".format(iteration))
    plt.pause(0.1) # pause the program for 0.5 second; if graph changes too quickly, increase this value; you can also speed up the process by decreasing this value
    for particle in particles:
      # update personal best
      particle.update_personal_best()
      # update global best
      if global_best_position == None:
        global_best_position = particle.position
      else:
        global_best_position = compareFitness(global_best_position, particle.position)
    global_best_position_list.append(global_best_position) # take note on the indentation
    # generate beta randomly for current iteration
    beta = [random.random(), random.random()]
    for particle in particles:
      # update velocity
      particle.update_velocity(alpha, beta, global_best_position)
      # update position
      particle.update_position(position_limits)
    iteration += 1
    #input()
  # display results
  print(iteration, [round(x.position,2) for x in particles])
  if len(space_ax.lines) > 1:
    del space_ax.lines[1]
  space_ax.plot([x.position for x in particles], [fitnessfunc(x.position) for x in particles], 'go')
  space_ax.set_title("Position of particles in iteration {}".format(iteration))
  

  [pos_fig, position_axes] = plt.subplots(4,1,sharex=True)
  position_axes[0].set_title("Position of each particle")
  position_axes[1].set_title("Fitness of each particle")
  position_axes[2].set_title("Boxplot of position at each iteration")
  position_axes[3].set_title("Boxplot of fitness at each iteration")
  position_axes[3].set_xlabel("Iteration")
  [vel_fig, velocity_axes] = plt.subplots(2,1,sharex=True)
  velocity_axes[0].set_title("Velocity of each particle")
  velocity_axes[1].set_title("Boxplot for velocity at each iteration")
  velocity_axes[1].set_xlabel("Iteration")
  [p_best_fig, personal_best_axes] = plt.subplots(4,1,sharex=True)
  personal_best_axes[0].set_title("Personal best position of each particle")
  personal_best_axes[1].set_title("Personal best fitness of each particle")
  personal_best_axes[2].set_title("Boxplot of personal best position at each iteration")
  personal_best_axes[3].set_title("Boxplot of personal best fitness at each iteration")
  personal_best_axes[3].set_xlabel("Iteration")
  [g_best_fig, global_best_axes] = plt.subplots(2,1,sharex=True)
  global_best_axes[0].set_title("Global best position")
  global_best_axes[1].set_title("Fitness for global best position")
  global_best_axes[1].set_xlabel("Iteration")
  for particle in particles:
    iteration_list = list(range(len(particle.position_list)))
    position_axes[0].plot(iteration_list, particle.position_list, '-o')
    position_axes[1].plot(iteration_list, [fitnessfunc(x) for x in particle.position_list], '-o')

    velocity_axes[0].plot(iteration_list, particle.velocity_list, '-o')

    personal_best_axes[0].plot(iteration_list[:-1], particle.best_position_list, '-o')
    personal_best_axes[1].plot(iteration_list[:-1], [fitnessfunc(x) for x in particle.best_position_list], '-o')

  position_axes[2].boxplot([[p.position_list[i] for p in particles] for i in iteration_list], positions=iteration_list)
  position_axes[3].boxplot([[fitnessfunc(p.position_list[i]) for p in particles] for i in iteration_list], positions=iteration_list)

  velocity_axes[1].boxplot([[p.velocity_list[i] for p in particles] for i in iteration_list], positions=iteration_list)

  personal_best_axes[2].boxplot([[p.best_position_list[i] for p in particles] for i in iteration_list[:-1]], positions=iteration_list[:-1])
  personal_best_axes[3].boxplot([[fitnessfunc(p.best_position_list[i]) for p in particles] for i in iteration_list[:-1]], positions=iteration_list[:-1])

  global_best_axes[0].plot(iteration_list[:-1], global_best_position_list, '-o')
  global_best_axes[1].plot(iteration_list[:-1], [fitnessfunc(x) for x in global_best_position_list], '-o')

  # plt.pause(0.1)
  plt.show()
  # input()

