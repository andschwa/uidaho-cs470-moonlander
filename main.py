#!/usr/local/bin/python

import sys

from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import HillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment

from tasks import LanderTask


def main():
    task = LanderTask()
    net = buildNetwork(task.indim, 5, task.outdim)
    agent = OptimizationAgent(net, HillClimber())
    experiment = EpisodicExperiment(task, agent)
    experiment.doEpisodes(100)


if __name__ == '__main__':
    sys.exit(main())
