#!/usr/local/bin/python

import sys

from pybrain.utilities import fListToString
from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import HillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment

from tasks import LanderTask


def main():
    task = LanderTask()
    net = buildNetwork(task.indim, 5, task.outdim)
    learner = HillClimber(storeAllEvaluations=True)
    agent = OptimizationAgent(net, learner)
    experiment = EpisodicExperiment(task, agent)
    experiment.doEpisodes(100)
    print('Episodes learned from {}'.format(len(learner._allEvaluations)))
    n, fit = learner._bestFound()
    print('Best fitness found: {}, with this network: {}'.format(fit, n))
    print('Containing these parameters: {}'.format(fListToString(n.params, 7)))


if __name__ == '__main__':
    sys.exit(main())
