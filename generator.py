import math
import particledata

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
    def __init__(self, xmin, xmax, ymin, ymax, b) -> None:
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.b = b
    
    def __repr__(self):
        return f"Env({self.xmin}, {self.xmax}, {self.ymin}, {self.ymax}, {self.b})"

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
    t = min(xint, yint)
    return x + t*vx, y+t*vy

class LinePath:
    def __init__(self, x1, y1, x2, y2):
        self.mode = "line"
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    
    def __repr__(self):
        return f"LinePath({self.x1}, {self.y1}, {self.x2}, {self.y2})"

class CirclePath:
    def __init__(self, x, y, r, t1, t2):
        self.mode = "circle"
        self.x=x
        self.y=y
        self.r=r
        self.t1=t1
        self.t2=t2
    
    def __repr__(self):
        return f"CirclePath({self.x}, {self.y}, {self.r}, {self.t1}, {self.t2})"

class Trail:
    def __init__(self, particle, path):
        self.label = particle.name
        self.path = path
    
    def __repr__(self):
        return f"Trail({self.label}, {self.path})"

def propagate(particle, x, y, px, py, env):
    # TODO: Consider interactions! This code only models motion for now
    if particle.mass == 0:
        # For now, the particle moves to the edge of the bounds
        x2, y2 = lineBounds(x, y, px, py, env)
        return [Trail(particle, LinePath(x, y, x2, y2))]
    else:
        p = math.sqrt(px**2+py**2)
        dx, dy = px/p, py/p # Unit vector direction of travel
        rg = p / (particle.charge * env.b) # Gyroradius calculation
        # Positive indicates clockwise, negative indicates counterlockwise
        # TODO: Check direction of circle with respect to magnetic field
        cx, cy = -dy*rg+x, dx*rg+y # Gyrocenter calculation
        return [Trail(particle, CirclePath(cx, cy, rg, 0, 2*math.pi))]