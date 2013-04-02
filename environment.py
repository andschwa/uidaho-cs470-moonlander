import random

from pybrain.rl.environments.environment import Environment


class Lander(Environment):
    max_safe_landing_speed = 4.0
    min_safe_x = -0.2
    max_safe_x = 0.2

    def __init__(self):
        self.reset()

    def reset(self):
        self.acceleration = random.randint(10, 30)/10  # 1-3 by 0.1
        self.wind = 0.2 * random.random()

        self.status = 'in_air'
        self.height = 100.0
        self.x_position = 0
        self.y_velocity = 10.0 * random.random()
        self.x_velocity = 0
        self.fuel = 100.0
        self.burn = None
        self.thrust = None

    def performAction(self, action):
        self.burn, self.thrust = action

        self.y_velocity += self.acceleration

        if self.fuel < self.burn:
            self.burn = self.fuel
        self.fuel -= abs(self.burn)
        self.y_velocity -= self.burn

        if self.fuel < self.thrust:
            self.thrust = self.fuel
        self.fuel -= abs(self.thrust)
        self.x_velocity -= self.thrust

        self.height -= self.y_velocity
        self.x_position += self.x_velocity + self.wind
        self._getStatus()

    def _getStatus(self):
        if self.height > 0:
            return 'in_air'
        if (self.y_velocity > self.max_safe_landing_speed or
                self.x_position < self.min_safe_x or
                self.x_position > self.max_safe_x):
            return 'crashed'
        else:
            return 'landed'

    def getSensors(self):
        return (self.height,
                self.x_position,
                self.y_velocity,
                self.x_velocity,
                self.wind,
                self.acceleration,
                self.fuel)

    def printResults(self):
        output = {'Status': self.status,
                  'Height': self.height,
                  'Y-Velocity': self.y_velocity,
                  'Position': self.x_position,
                  'X-Velocity': self.x_position,
                  'Fuel': self.fuel}
        for string, variable in output.iteritems():
            print(string + ': {0}'.format(variable))
