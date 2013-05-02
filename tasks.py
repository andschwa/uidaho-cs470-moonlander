from math import ceil
from pybrain.rl.environments import EpisodicTask
from environment import Lander


class LanderTask(EpisodicTask):
    """
    Task that represents lander attempting to land.
    """

    def __init__(self, environment=None):
        if environment is None:
            self.env = Lander()
        else:
            self.env = environment
        EpisodicTask.__init__(self, self.env)

        self.sensor_limits = [(0.0, 100.0), (0.0, 25.0), (1.0, 3.0),
                              (-1.0, 1.0), (-1.0, 1.0),
                              (-0.1, 0.1), (0.0, 100.0)]
        self.actor_limits = [(0.0, 10.0), (-1.0, 1.0)]

    def isFinished(self):
        return self.env.status == 'landed' or self.env.status == 'crashed'

    def getReward(self):
        reward = 0
        if self.env.status == 'crashed':
            if self.env.y_velocity > self.env.max_safe_landing_speed:
                error = ceil(abs(self.env.y_velocity) /
                               self.env.max_safe_landing_speed)
                reward -= error*error
            if abs(self.env.x_position) > self.env.max_safe_x:
                error = ceil(abs(self.env.x_position) /
                               self.env.max_safe_x)
                reward -= error*error
            print('Returning full crashed reward: {}'.format(reward))
        if self.env.status == 'landed':
            reward += 5000
        return reward
