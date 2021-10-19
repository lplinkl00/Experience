import random 
## Particle Swarm Optimization
class Particle:
    def __init__(self, position = 0, velocity = 0):
        self.position = position
        self.velocity = velocity
        self.best_position = position

    def update_personal_best(self):
        c_position = fit_fcn()
        b_position = self.best_position
        if c_position < b_position:
            self.best_position = c_position
        else:
            self.best_position = b_position

    def update_velocity(self, alpha, beta, global_best_position):
        alpha_1 = alpha[0]
        alpha_2 = alpha[1]
        beta_1 = beta[0]
        beta_2 = beta[1]
        t = global_best_position
        q = self.best_position
        p = self.position
        v = self.velocity
        nv = v + ((alpha_1 * beta_1)*(q - p)) + ((alpha_2 * beta_2)*(t - p))
        self.velocity = nv
    
    def update_position(self, position_limits):
        lower = position_limits[0]
        upper = position_limits[1]
        if lower <self.position < upper:
            self.position = self.position + self.velocity
        else:
            print("position out of bounds")
            self.position = self.position

    

def fit_fcn(position):
    x = position
    if (-100 <= x < 100):
        fitness = (x + 100)*(x+50)*(x)*(x-20)*(x-60)*(x-100)
    else:
        print("error position is out of bounds")
    return fitness

def initialise_particles(n_ptc, position_limits):
    part_list = []
    part_list.append(Particle(0,0))
    for i in range(n_ptc):
        position = random.randint(position_limits[0], position_limits[1])
        velocity = 0
        part_list.append(Particle(position, velocity))
    particles = part_list
    return [Particle.position for Particle in particles]

def compareFitness(pos1, pos2):
    if pos1 < pos2:
        betterpos = pos1
    else:
        betterpos = pos2
    return betterpos

def calc_avg_fit_diff(particles):
  # 1. calculate mean fitness of all particles
    total_fitness = 0
    mse = 0
    for i in particles:
        temp_fit = fit_fcn(i)
        total_fitness = total_fitness + temp_fit
    mean_fitness = total_fitness/len(particles)    
  # 2. calculate the difference between the mean fitness and the fitness of each particle
    for i in particles:
        temp_fit = fit_fcn(i)
        mse = mse + (temp_fit - mean_fitness)
  # 3. calculate the average of the differences obtained from step 2
    avg_fit_diff = mse/len(particles)
    return avg_fit_diff


def calc_avg_pos_diff(particles):
  # 1. calculate mean position of all particles
    total_positions = 0
    for i in particles:
        temp_pos = i.position
        total_positions = total_positions + temp_pos
    mean_pos = total_positions/len(particles)
  # 2. calculate the difference between the mean position and the position of each particle
    for i in particles:
        temp_pos = i.position
        mse = mse + (temp_pos - mean_pos)
  # 3. calculate the average of the differences obtained from step 2
    avg_pos_diff = mse/len(particles)
    return avg_pos_diff


if __name__ == '__main__':
    max_iter = 200
    alpha = [0.1, 0.1]
    n_particle = 10
    global_best_position = None
    position_limits = [-100, 100]
    iteration = 0
    avg_pos_diff = 0
    avg_fit_diff = 0
    min_avg_fit_diff = 0.1
    min_avg_pos_diff = 0.1
    particles = initialise_particles(n_particle,position_limits)
    while (iteration < max_iter or avg_pos_diff > min_avg_pos_diff or avg_fit_diff > min_avg_fit_diff):
        print(iteration, [round(x.position,2) for x in particles])
        for particle in particles:
            # update personal best
            particle.update_personal_best()
            # update global best
            if global_best_position == None:
                global_best_position = particle.position
            else:
                global_best_position = compareFitness(global_best_position, particle.position)
             # generate beta randomly for current iteration
        beta = [random.random(), random.random()]
        for particle in particles:
            # update velocity
            particle.update_velocity(alpha, beta, global_best_position)
            # update position
            particle.update_position(position_limits)
        iteration += 1
    # display results
    print(iteration, [round(x.position,2) for x in particles])

    


    


