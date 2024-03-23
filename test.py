from particledata import *
from generator import *

env = Env(-100, 100, -100, 100, 1)

print(propagate(POSITRON, 0, 0, 100, 0, env)[0])
print(propagate(ELECTRON, 0, 0, 100, 0, env)[0])