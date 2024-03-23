/**
 * Sampling from an exponential distribution
 * 
 * Formula from https://www.baeldung.com/cs/sampling-exponential-distribution
 * 
 * @param {*} lambda The lambda parameter of the exponential
 * @returns A sample drawn from the exponential distribution
 */
function expSample(lambda) {
    return -1/lambda * Math.log(1-Math.random());
}

/**
 * The relativistic velocity-momentum formula
 * 
 * @param {*} p Momentum
 * @param {*} m Mass of particle
 */
function vel(p, m) {
    return Math.sqrt(1/((m) + 1))
}

class Env {
    /**
     * An object representing an environment
     * 
     * @param {*} xmin The lower bound on x
     * @param {*} xmax The upper bound on x
     * @param {*} ymin The lower bound on y
     * @param {*} ymax The upper bound on y
     */
    constructor(xmin, xmax, ymin, ymax) {
        this.xmin = xmin;
        this.xmax = xmax;
        this.ymin = ymin;
        this.ymax = ymax;
    }
}

/**
 * Computes the point at which a particle moving in a straight line will exit a particular rectangular bounds
 * 
 * @param {*} x The initial x-position of the particle
 * @param {*} y The initial y-position of the particle
 * @param {*} vx The x-velocity of the particle
 * @param {*} vy The y-velocity of the particle
 * @param {*} env The environment the particle is moving in
 * @returns An array consisting of the (x, y) position of the point of intersection
 */
function lineBounds(x, y, vx, vy, env) {
    var xint, yint;
    if (vx < 0) {
        xint = (env.xmin-x)/vx;
    }
    else {
        xint = (env.xmax-x)/vx;
    }
    if (vy < 0) {
        yint = (env.ymin-x)/vy;
    }
    else {
        yint = (env.ymax-y)/vy
    }
    let t = Math.min(xint, yint);
    return [x + t*vx, y+t*vy];
}

class LinePath {
    constructor(x1, y1, x2, y2) {
        this.type = "line"
        this.params = {
            x1: x1,
            y1: y1,
            x2: x2,
            y2: y2
        }
    }
}

class Trail {
    constructor(particle, path) {
        this.label = particle.name;
        this.path = path;
    }
}

/**
 * Computes the tracks created by a particle, recursively calling itself for decay products
 * 
 * @param {*} particle Identity of the particle considered
 * @param {*} x Particle's x position
 * @param {*} y Particle's y position
 * @param {*} px Particle's x momentum
 * @param {*} py Particle's y momentum
 * @param {*} env Environment the particle is moving in
 * @returns Array of track objects
 */
function propagate(particle, x, y, px, py, env) {
    if (particle.mass == 0) {
        // TODO: Consider interactions!
        // For now, we assume the particle moves to the edge of the bounds unimpeded
        [x2, y2] = lineBounds(x, y, px, py, env)
        return [new Trail(particle, new LinePath(x, y, x2, y2))];
    }
    else {
        // wtf
    }
}