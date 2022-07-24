from functools import wraps

from game.engine.market import CostMaker


class Engine:
    def __init__(self):
        self.clips = 0
        self._total_clips = 0
        self.wire = 100
        self.money = 10
        self.actions = ['make_clip', 'buy_wire', 'sell']
        self._n_actions = len(self.actions)

        self.cost_maker = CostMaker()

        self.callbacks = []
        self.add_callback(self.cost_maker.update)

    def time_step(func):
        """
        Wrapper for every time-consuming action
        :return:
        """
        @wraps(func)
        def inner(self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            self.__wellcallyouback()

            return res
        return inner

    def add_callback(self, func: callable):
        """Adds a function to list of callbacks"""
        self.callbacks.append(func)

    def __wellcallyouback(self):
        """Calls all callback functions on every game update step"""
        for func in self.callbacks:
            func()

    @time_step
    def make_clip(self):
        if self.wire > 0:
            self.clips += 1
            self._total_clips += 1
            self.wire -= 1

    @time_step
    def buy_wire(self):
        if self.money > self.cost_maker.cost:
            self.money -= self.cost_maker.cost
            self.wire += 100

    @time_step
    def sell(self):
        if self.clips > 0:
            self.clips -= 1
            self.money += 1

    def __str__(self):
        return f"""Clips: {self.clips}\nWire: {self.wire}\nMoney: {self.money}"""

