import numpy as np

class Rigidbody():
    def __init__(
                    self,
                    mass=0.0,
                    position=np.array([0.0,0.0,0.0]),
                    velocity=np.array([0.0,0.0,0.0]),
                    fps=60,
                ):
        
        # external
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.fps = fps
        self.dt = 1/self.fps
        
        # internal
        self.gravity_true = True
        self.friction_true = True
        
        self.Earth_Gravity = 9.81 # m/s**2
        self.Relative_Gravity = 1
        self.Gravity = self.Earth_Gravity * self.Relative_Gravity
        
        self.Friction_Coefficient = 0.42
        self.Friction = self.Friction_Coefficient * self.mass * self.Relative_Gravity * self.dt
        
    def friction(self):
        if self.velocity[0] > 0:
            self.velocity[0] += -self.Friction
        if self.velocity[0] < 0:
            self.velocity[0] += self.Friction
        if self.velocity[2] > 0:
            self.velocity[2] += -self.Friction
        if self.velocity[2] < 0:
            self.velocity[2] += self.Friction
    
    def update(self,force):
        if self.gravity_true:
            force[1] += self.Gravity
        if self.friction_true:
            self.friction()
        
        acceleration = force / self.mass
        self.velocity += acceleration * self.dt
        self.position += self.velocity * self.dt + 0.5 * acceleration * self.dt * self.dt
        
        
        return self.position
        