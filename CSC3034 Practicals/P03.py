import random 
## Particle Swarm Optimization
class Particle:
    def __init__(self, position = 0, velocity = 0):
        self.position = position
        self.velocity = velocity
        self.best_position = position

    def update_personal_best(self):
        position = fit_fcn()


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
        position = random.uniform(position_limits[0], position_limits[1])
        velocity = 0
        part_list.append(Particle(velocity, position))
    particles = part_list
    return [Particle.position for Particle in particles]


if __name__ == '__main__':
    alpha = [0.1, 0.1]
    n_particle = 10
    print(initialise_particles(10,[0,10]))
