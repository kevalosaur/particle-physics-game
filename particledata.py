class ParticleType:
    """
    Represents a type of particle.
    """

    def __init__(self, name, mass, charge, decays, halflife, decayPattern):
        """
        Constructs an object representing a type of particle.
        
        :param name: Name of the particle.
        :param mass: Rest mass of the particle.
        :param charge: Charge of the particle.
        :param decays: Boolean, whether the particle decays.
        :param halflife: Half-life of the particle.
        :param decayPattern: List of possible decay modes, with weights.
        """
        self.name = name
        self.mass = mass
        self.charge = charge
        self.decays = decays
        self.halflife = halflife
        self.decayPattern = decayPattern


class DecayMode:
    def __init__(self, products, weight):
        self.products = products
        self.weight = weight


ELECTRON = ParticleType("e-", 1, -1, False, None, [])
POSITRON = ParticleType("e+", 1, +1, False, None, [])
PHOTON = ParticleType("y", 0, 0, False, None, [])
