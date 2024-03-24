import particledata
from pyscript import document

buttondiv = document.querySelector('#buttons')

for particle in particledata.PARTICLES:
    particle = particledata.PARTICLES[particle]
    buttondiv.innerHTML += f'<button id={particle.ident}>{particle.symbol}</button>'