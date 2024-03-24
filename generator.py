import math
import random
from particledata import *
from diagramtosvg import curve_func
from pyscript import window

c = 299.792458

def expSample(l):
    """
    Sampling from an exponential distribution

    Formula from https://www.baeldung.com/cs/sampling-exponential-distribution
    
    :param l: The lambda parameter of the exponential
    :return: An sample drawn from the exponential distribution
    """
    return -1/l * math.log(1-random.random())

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
    :return: A tuple consisting of the (x, y) position of the point of intersection
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

# def circleBounds(x, y, r, env):
#     """
#     Computes the point at which a circular path exits the bounding circle of the environment

#     :param x: The x-position of the center
#     :param y: The y-position of the center
#     :param r: The radius of the circle
#     :param env: The environment the particle is moving in
#     :return: A tuple containing the two theta-values at which the circles intersect. If they do not, returns None
#     """
#     pass



class LinePath:
    def __init__(self, x1, y1, x2, y2):
        self.mode = "line"
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    
    def __repr__(self):
        return f"LinePath({self.x1}, {self.y1}, {self.x2}, {self.y2})"

# class CirclePath:
#     def __init__(self, x1, y1, x2, y2, r, isCCW, isOverPi):
#         self.mode = "circle"
#         self.x1=x1
#         self.y1=y1
#         self.x2=x2
#         self.y2=y2
#         self.r=r
#         self.isCCW = isCCW
#         self.isOverPi = isOverPi
    
#     def __repr__(self):
#         return f"CirclePath({self.x1}, {self.y1}, {self.x2}, {self.y2}, {self.r}, {self.isCCW}, {self.isOverPi})"

class SpiralPath:
    def __init__(self, x, y, r, curve_sign, t0, t, a):
        self.mode = "spiral"
        self.x = x
        self.y = y
        self.r = r
        self.curve_sign = curve_sign
        self.t0 = t0
        self.t = t
        self.a = a
    
    def __repr__(self):
        return f"SpiralPath({self.x}, {self.y}, {self.r}, {self.curve_sign}, {self.t0}, {self.t}, {self.a})"

class Trail:
    def __init__(self, particle, path):
        self.label = particle.ident
        self.path = path
    
    def __repr__(self):
        return f"Trail({self.label}, {self.path})"

def decay_momentum(M, m1, m2):
    return math.sqrt((M**2 - (m1+m2)**2)*(M**2-(m1-m2)**2)) / (2 * M)

def random_angles(steps = 1):
    theta = random.random() * 2 * math.pi
    step_size = 2*math.pi / steps
    return [(math.cos(theta+step_size*i), math.sin(theta+step_size*i)) for i in range(steps)]

def propagate(particle, x, y, px, py, env, force_decay = None):
    # TODO: Consider interactions! This code only models motion for now
    p = math.sqrt(px**2+py**2)
    if particle.decays:
        if force_decay:
            decay_time = None
            decay_dist = random.random()*100+50
        else:
            decay_time = expSample(1/particle.meanlife)
            decay_dist = decay_time * p / particle.mass * c
        window.console.log(decay_time, decay_dist)
    if particle.mass == 0:
        # For now, the particle moves to the edge of the bounds
        x2, y2 = lineBounds(x, y, px, py, env)
        return [Trail(particle, LinePath(x, y, x2, y2))]
    else:
        dx, dy = px/p, py/p # Unit vector direction of travel
        rg = p / (particle.charge * env.b) # Gyroradius calculation
        # Sign is correct if positive B means out of page
        cx, cy = -dy*rg+x, dx*rg+y # Gyrocenter calculation
        curve_sign = 1 if rg > 0 else -1 # negative means CCW
        rg = abs(rg)
        td = (math.asin(dy) if dx>0 else math.pi - math.asin(dy))
        t0 = td - math.pi/2 * curve_sign
        other = []
        a = 0.1
        if particle.decays:
            angle_moved = decay_dist/rg
            px2 = px*math.cos(angle_moved)-py*math.sin(angle_moved)*curve_sign
            py2 = px*math.sin(angle_moved)*curve_sign+py*math.cos(angle_moved)
            daughters = [PARTICLES[d] for d in particle.decayPattern[0].products] # TODO: Random choice here? Not really relevant
            energy_out = particle.mass - sum([d.mass for d in daughters])
            momentum = decay_momentum(particle.mass, daughters[0].mass, daughters[1].mass)
            xs, ys = curve_func(angle_moved, rg, a)*math.cos(curve_sign*angle_moved+t0)+cx, curve_func(angle_moved, rg, a)*math.sin(curve_sign*angle_moved+t0)+cy
            angles = random_angles(steps=len(daughters))
            for i, daughter in enumerate(daughters):
                other += propagate(daughter, xs, ys, px2 + momentum*angles[i][0], py2+momentum*angles[i][1], env)
        else:
            angle_moved = 30*math.pi # TODO: This should be calculated somehow
        return other + [Trail(particle, SpiralPath(cx, cy, rg, curve_sign, t0, angle_moved, a))]
