from pybrain.rl.environments import EpisodicTask
from environment import Lander


class LanderTask(EpisodicTask):
    """
    Task that represents lander attempting to land.
    """

    def __init__(self, environment=None):
        if environment is None:
            environment = Lander()
        self.env = environment
        EpisodicTask.__init__(self, environment)

        self.sensor_limits = [(0.0, 100.0), (0.0, 35.0), (1.0, 3.0),
                              (-0.2, 0.2), (-0.2, 0.2),
                              (-0.1, 0.1), (0.0, 100.0)]
        self.actor_limits = [(0.0, 12.0), (-0.1, 0.1)]

    def isFinished(self):
        return self.env.status == 'landed' or self.env.status == 'crashed'

    def performAction(self, action):
        EpisodicTask.performAction(self, action)

    def getReward(self):
        reward = 0
        if self.env.status == 'in_air':
            if abs(self.env.x_position) > self.env.max_safe_x:
                reward -= 1
            if self.env.y_velocity > 25:
                reward -= 1
        if self.env.status == 'crashed':
            if self.env.y_velocity > self.env.max_safe_landing_speed:
                reward -= 100
            if abs(self.env.x_position) > self.env.max_safe_x:
                reward -= 100
        if self.env.status == 'landed':
            reward += 1000
        return reward
