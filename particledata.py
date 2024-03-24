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


ELECTRON = ParticleType("e-", "e-", 0.511, -1, False, None, [],
"The electron, e-, is a component of ordinary matter, found orbiting atomic nuclei. A high-energy electron is called a beta ray. Electrons leave thin trails in the detector.")
POSITRON = ParticleType("ep", "e+", 0.511, +1, False, None, [],
"The positron, e+, is the antimatter counterpart of the electron, with equal mass but inverted charge. A positron will leave an electron-like trail, but curving in the opposite direction.")
PHOTON = ParticleType("y", "γ", 0, 0, False, None, [],
"The photon, γ, is the carrier of the electromagnetic force and a particle of light. Depending on energy and source they can be referred to as gamma rays or X-rays. Photons are neutral and thus leave no trail in the bubble chamber.")
MUON = ParticleType("mu", "μ-", 105.658, -1, True, 2.197e-6, [DecayMode(["e-", "ve bar", "vmu"])],
"The muon, μ-, is a so-called \"heavy electron\", having the same charge as the electron but being over 200 times more massive. They are unstable and decay into electrons. They leave thick trails in the detector.")

PARTICLES = [ELECTRON, POSITRON, PHOTON, MUON]

