import numpy as np

from .base_agent import BaseAgent


class RandomAgent(BaseAgent):

    def __call__(self, state):
        return np.random.choice(self.actions)
