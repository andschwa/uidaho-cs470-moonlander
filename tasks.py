from math import ceil
from pybrain.rl.environments import EpisodicTask
from environment import Lander


class LanderTask(EpisodicTask):
    """
    Task that represents lander attempting to land.
    """

    def __init__(self, environment=None, batchSize=1):
        self.batchSize = batchSize
        if environment is None:
            self.env = Lander()
        else:
            self.env = environment
        EpisodicTask.__init__(self, self.env)

        self.sensor_limits = [(0.0, 200.0), (0.0, 35.0), (0.0, 4.0),
                              (-6.0, 6.0), (-0.4, 0.4),
                              (-0.15, 0.15), (0.0, 200.0)]

    def isFinished(self):
        return self.env.status == 'landed' or self.env.status == 'crashed'

    def getReward(self):
        reward = 0
        if self.env.status == 'crashed':
            if self.env.y_velocity > self.env.max_safe_landing_speed:
                error = ceil(abs(self.env.y_velocity) /
                             self.env.max_safe_landing_speed)
                reward -= error
            if abs(self.env.x_position) > self.env.max_safe_x:
                error = ceil(abs(self.env.x_position) /
                             self.env.max_safe_x)
                reward -= error
        if self.env.status == 'landed':
            reward = 1
        print('Reward: {}'.format(reward))
        return reward
