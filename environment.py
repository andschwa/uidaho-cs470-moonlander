import random

from pybrain.rl.environments.environment import Environment
from scipy import asarray


class Lander(Environment):
    indim = 7
    outdim = 2

    max_safe_landing_speed = 4.0
    max_safe_x = 0.2

    def __init__(self):
        self.acceleration = float(random.randint(10, 30))/10  # 1-3 by 0.1
        self.wind = 0.2 * (random.random()-0.5)
        self.y_velocity_offset = 10.0 * random.random()
        self.reset()

    def reset(self):
        self.status = 'in_air'
        self.height = 100.0
        self.x_position = 0.0
        self.x_velocity = 0.0
        self.y_velocity = self.y_velocity_offset
        self.fuel = 100.0
        self.sensors = [self.height,
                        self.y_velocity,
                        self.acceleration,
                        self.x_position,
                        self.x_velocity,
                        self.wind,
                        self.fuel]

    def performAction(self, action):
        burn, thrust = action

        self.y_velocity += self.acceleration
        if self.fuel < abs(burn):
            burn = self.fuel
        self.fuel -= abs(burn)
        self.y_velocity -= burn

        if self.fuel < abs(thrust):
            if thrust > 0:
                thrust = self.fuel
            elif thrust < 0:
                thrust = -self.fuel
        self.fuel -= abs(thrust)
        self.x_velocity -= thrust

        self.height -= self.y_velocity
        self.x_position += self.x_velocity + self.wind
        self.status = self._getStatus()
        self.output(burn, thrust)

    def _getStatus(self):
        if self.height > 0:
            return 'in_air'
        elif (self.y_velocity > self.max_safe_landing_speed or
                abs(self.x_position) > self.max_safe_x):
            return 'crashed'
        else:
            return 'landed'

    def getSensors(self):
        return asarray(self.sensors)

    def output(self, burn, thrust):
        output = {'Status': self.status,
                  'Height': self.height,
                  'Y-Velocity': self.y_velocity,
                  'Burn': burn,
                  'Wind': self.wind,
                  'X-Velocity': self.x_velocity,
                  'X-Position': self.x_position,
                  'Thrust': thrust,
                  'Fuel': self.fuel}
        for string, variable in output.items():
            print(string+': {}'.format(variable))
        print('')
