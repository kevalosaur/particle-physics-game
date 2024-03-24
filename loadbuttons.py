import particledata
from pyscript import document

buttondiv = document.querySelector('#buttons')

for particle in particledata.PARTICLES:
    buttondiv.innerHTML += f'<button id={particle.ident}>{particle.symbol}</button>'