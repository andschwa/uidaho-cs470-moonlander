from pybrain.rl.environments import EpisodicTask


class LanderTask(EpisodicTask):
    """
    Task that represents lander attempting to land.
    """
    defaultReward = 0
    crashedPenalty = -1
    landed = 1

    def __init__(self, environment):
        EpisodicTask.__init__(self, environment)
        self.reset()

    def isFinished(self):
        status = self.env.status == 'landed' or self.env.status == 'crashed'
        if status:
            self.env.printResults()
        return status

    def getReward(self):
        if self.env.status == 'in_air':
            return self.defaultReward
        if self.env.status == 'crashed':
            return self.crashedPenalty
        if self.env.status == 'landed':
            return self.landedReward
