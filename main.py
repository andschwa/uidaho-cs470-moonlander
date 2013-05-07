#!/usr/local/bin/python

import sys

from pybrain.tools.shortcuts import buildNetwork
from pybrain.optimization import StochasticHillClimber
from pybrain.rl.agents import OptimizationAgent
from pybrain.rl.experiments import EpisodicExperiment

from tasks import LanderTask
from environment import Lander


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
    task = LanderTask(batchSize=1)
    net = buildNetwork(task.indim, 5, task.outdim)
    learner = StochasticHillClimber()
    agent = OptimizationAgent(net, learner)
    experiment = EpisodicExperiment(task, agent)
    experiment.doEpisodes(100000)

    tasks = [LanderTask(environment=Lander(acceleration=float(i)))
             for i in range(1, 4)]
    test_size = 1000
    for task in tasks:
        print("Running task with acceleration {}".format(task.env.acceleration))
        success = 0
        for _ in range(test_size):
            task.env.reset()
            while not task.isFinished():
                observation = task.getObservation()
                action = net.activate(observation)
                task.performAction(action)
            print("Finished a simulation with result {}".format(task.env.status))
            if task.env.status == 'landed':
                success += 1
        print("Succeeded {} times out of {}".format(success, test_size))


if __name__ == '__main__':
    sys.exit(main())
