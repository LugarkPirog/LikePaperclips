import numpy as np

from common import StatTracer


class CostMaker:
    def __init__(self):
        self.mean = 18
        self.std = 5
        self.p_change = 0.3
        self.cost = self.mean

        self.steps = 0

        self.st = StatTracer()

    def update(self):
        self.st.log('update')
        self.steps += 1
        if np.random.random() < self.p_change:
            self.cost = np.random.randn() * self.std + self.mean
