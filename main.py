from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram
import random

window.console.log("test!")

env = Env(-1000, 1000, -1000, 1000, 1)

test_object = []

for _ in range(random.randint(1, 3)):
    ident = random.choice(["e_n", "e_p", "mu_n", "mu_p"])
    x, y, px, py = random.random() * 100 - 100, random.random() * 100 - 100, random.random() * 300 - 100, random.random() * 300 - 100
    # t = random.random() * 2 * math.pi
    # px += 40*math.cos(t)
    # py += 40*math.sin(t)
    test_object += propagate(PARTICLES[ident], x, y, px, py, env)

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)