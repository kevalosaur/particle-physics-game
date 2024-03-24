from particledata import *
from generator import *

env = Env(-100, 100, -100, 100, 1)

test_object = propagate(ELECTRON, -50, 60, 30, 45, env) \
            + propagate(POSITRON, -50, 60, 15, 20, env)

print(test_object)