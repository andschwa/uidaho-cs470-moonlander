from pybrain.rl.environments import EpisodicTask
from environment import Lander


class LanderTask(EpisodicTask):
    """
    Task that represents lander attempting to land.
    """

    def __init__(self, environment=None):
        if environment is None:
            environment = Lander()
        EpisodicTask.__init__(self, environment)

        self.defaultReward = 0
        self.crashedPenalty = -1
        self.landed = 1

        self.sensor_limits = [(0, 100), (1, 30), (1, 3),
                              (-1, 1), (-3, 3), (-1, 1), (0, 100)]
        self.actor_limits = [(0, 9), (-3, 3)]

    def isFinished(self):
        return self.env.status == 'landed' or self.env.status == 'crashed'

    def getReward(self):
        if self.env.status == 'in_air':
            return self.defaultReward
        if self.env.status == 'crashed':
            return self.crashedPenalty
        if self.env.status == 'landed':
            return self.landedReward
