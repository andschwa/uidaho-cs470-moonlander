#!/usr/local/bin/python

import sys

from pybrain.rl.learners.valuebased import ActionValueNetwork
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import NFQ
from pybrain.rl.experiments import EpisodicExperiment

from environment import Lander
from tasks import LanderTask


def main():
    environment = Lander()
    controller = ActionValueNetwork(7, 121)
    learner = NFQ()
    agent = LearningAgent(controller, learner)
    task = LanderTask(environment)
    experiment = EpisodicExperiment(task, agent)

    for episodes in range(10):
        experiment.doEpisodes(1)
        agent.learn(1)
        print('Agent has learned {0} episodes.'.format(episodes + 1))


if __name__ == '__main__':
    sys.exit(main())
