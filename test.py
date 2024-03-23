from particledata import *
from generator import *

env = Env(-100, 100, -100, 100, 100)

print(propagate(PHOTON, -50, 60, 100, 20, env) + propagate(POSITRON, -50, 60, 100, 30, env) + propagate(ELECTRON, -50, 60, 90, 40, env))