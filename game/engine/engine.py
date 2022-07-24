import numpy as np

from game.engine.market import CostMaker


class Engine:
    def __init__(self):
        self.replay = []
        self.clips = 0
        self.__total_clips = 0
        self.wire = 100
        self.money = 10
        self.actions = ['make_clip', 'buy_wire', 'sell']
        self._n_actions = len(self.actions)

        self.cost_maker = CostMaker()

        self.callbacks = []
        self._fill_callbacks()

    def _fill_callbacks(self):
        self.callbacks.append(self.cost_maker.update)

    def __wellcallyouback(self):
        for func in self.callbacks:
            func()

    def make_clip(self):
        if self.wire > 0:
            self.clips += 1
            self.__total_clips += 1
            self.wire -= 1

    def buy_wire(self):
        if self.money > self.cost_maker.cost:
            self.money -= self.cost_maker.cost
            self.wire += 100

    def sell(self):
        if self.clips > 0:
            self.clips -= 1
            self.money += 1

    @property
    def state(self):
        return self.clips, self.wire, self.money

    def current_reward(self):
        return np.log(self.__total_clips + 1)

    def add_to_replay(self, state, action, reward):
        self.replay.append((state, action, reward))

    def __call__(self, pos):
        assert pos < self._n_actions

        # call all the global callbacks
        self.__wellcallyouback()

        # update state
        getattr(self, self.actions[pos])()
        self.add_to_replay(self.state, pos, self.current_reward())

    def __str__(self):
        return f"""Clips: {self.clips}\nWire: {self.wire}\nMoney: {self.money}"""

