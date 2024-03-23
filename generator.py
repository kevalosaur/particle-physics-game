import math

def expSample(l):
    """
    Sampling from an exponential distribution

    Formula from https://www.baeldung.com/cs/sampling-exponential-distribution
    
    :param l: The lambda parameter of the exponential
    :return: An sample drawn from the exponential distribution
    """
    return -1/l * math.log(1-math.random())

def vel(p, m):
    """
    The relativistic velocity-momentum formula

    :param p: Momentum
    :param m: Mass of particle
    :return: The velocity, in fractions of c
    """
    return math.sqrt(1/((m) + 1))

class Env:
    def __init__(self, xmin, xmax, ymin, ymax) -> None:
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

def lineBounds(x, y, vx, vy, env):
    """
    Computes the point at which a particle moving in a straight line will exit a particular rectangular bounds
    
    :param x: The initial x-position of the particle
    :param y: The initial y-position of the particle
    :param vx: The x-velocity of the particle
    :param vy: The y-velocity of the particle
    :param env: The environment the particle is moving in
    :return: An array consisting of the (x, y) position of the point of intersection
    """
    xint, yint = None, None
    if (vx < 0):
       xint = (env.xmin-x)/vx
    else:
        xint = (env.xmax-x)/vx
    if (vy < 0):
        yint = (env.ymin-x)/vy
    else:
        yint = (env.ymax-y)/vy
    t = math.min(xint, yint)
    return x + t*vx, y+t*vy

class LinePath:
    def __init__(self, x1, y1, x2, y2):
        self.type = "line"
        self.params = dict(
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2
        )

class Trail:
    def __init__(self, particle, path):
        this.label = particle.name
        this.path = path

def propagate(particle, x, y, px, py, env):
    if particle.mass == 0:
        # TODO: Consider interactions!
        # For now, the particle moves to the edge of the bounds
        x2, y2 = lineBounds(x, y, px, py, env)
        return [Trail(particle, LinePath(x, y, x2, y2))]
    else:
        # TODO: Continue this
        pass