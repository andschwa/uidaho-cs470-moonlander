#!/usr/local/bin/python

import sys

from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import StochasticHillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment

from tasks import LanderTask


def main():
    """
    The task represents one full simulation. Therefore it is episodic.
    Each episode calls performAction after passing getObservation to the agent.
    Once isFinished is true, the reward is returned and one simulation is done.

    The net is the neural network. It has 7 input nodes, a hidden layer of 5
    nodes, and 2 output nodes. It is a feed-forward network using sigmoid
    activation functions.

    OptimizationAgent(module, learner)
    EpisodicExperiment.optimizer = learner
    learner.setEvaluator(task, module)
    optimizer.learn()
    """
    task = LanderTask()
    net = buildNetwork(task.indim, 5, task.outdim)
    learner = StochasticHillClimber()
    agent = OptimizationAgent(net, learner)
    experiment = EpisodicExperiment(task, agent)
    experiment.doEpisodes(10000)


if __name__ == '__main__':
    sys.exit(main())
