class ParticleType {
    /**
     * Constructs an object representing a type of particle
     * 
     * @param {*} name Name of the particle
     * @param {*} mass Rest mass of the particle
     * @param {*} charge Charge of the particle
     * @param {*} decays Boolean, whether the particle decays
     * @param {*} halflife Half-life of the particle
     * @param {*} decayPattern List of possible decay modes, with weights
     */
    constructor(name, mass, charge, decays, halflife, decayPattern) {
        this.name = name;
        this.mass = mass;
        this.charge = charge;
        this.decays = decays;
        this.halflife = halflife;
        this.decayPattern = decayPattern;
    }
}

class DecayMode {
    constructor(products, weight) {
        this.products = products;
        this.weight = weight;
    }
}

ELECTRON = new ParticleType("e-", 1, -1, false, null, []);
PHOTON = new ParticleType("y", 0, 0, false, null, []);