import yaml

class ParticleType:
    """
    Represents a type of particle.
    """

    def __init__(self, ident, symbol, mass, charge, decays, meanlife, decayPattern, description):
        """
        Constructs an object representing a type of particle.
        
        :param name: Name of the particle.
        :param mass: Rest mass of the particle.
        :param charge: Charge of the particle.
        :param decays: Boolean, whether the particle decays.
        :param meanlife: Mean lifetime of the particle, AKA the time it takes for the population to 1/e
        :param decayPattern: List of possible decay modes, with weights.
        """
        self.ident = ident
        self.symbol = symbol
        self.mass = mass
        self.charge = charge
        self.decays = decays
        self.meanlife = meanlife
        self.decayPattern = decayPattern
        self.description = description
    
    def desc_text(self):
        return self.description + f"<em><br>Charge: {self.charge} e<br>Mass: {self.mass} MeV</em>"


class DecayMode:
    def __init__(self, products, weight=1):
        self.products = products
        self.weight = weight


with open("particles.yaml", "r") as file:
    PARTICLES = yaml.safe_load(file)
for k in PARTICLES:
    v = PARTICLES[k]
    decays = v['decays']
    if decays:
        meanlife = v['meanlife']
        modes = v['decaymodes']
        for i in range(len(modes)):
            modes[i] = DecayMode(modes[i]['products'], modes[i]['weight'])
    else:
        meanlife = None
        modes = None
    p = ParticleType(k, v['symbol'], v['mass'], v['charge'], decays, meanlife, modes, v['description'])
    PARTICLES[k] = p

print(PARTICLES)