import numpy as np

from game.engine import Engine


class BaseRLInterface:

    def __init__(self, engine):
        self.engine = engine
        self.replay = []

    def act(self, *args, **kwargs):
        """
        Returns new state and reward after taking action
        :param args:
        :param kwargs:
        :return: new_state, reward
        """
        pass

    def get_reward(self, *args, **kwargs):
        pass

    def get_state(self, *args, **kwargs):
        pass

    @property
    def state(self, *args, **kwargs):
        return self.get_state(*args, **kwargs)

    def add_to_replay(self, *args, **kwargs):
        pass


class EngineRLInterface(BaseRLInterface):

    def __init__(self):
        super().__init__(Engine())

    @property
    def actions(self):
        return self.engine.actions

    @property
    def state(self):
        return self.engine.clips, self.engine.wire, self.engine.money

    def get_reward(self, last_clips):
        """
        for Bandit we will construct the objective as follows:
        if total_clips increased after our action, then 1 else 0
        :return:
        """
        return int(self.engine._total_clips - last_clips > 0)

    def add_to_replay(self, state, action, reward):
        self.replay.append((state, action, reward))

    def act(self, action):
        assert action < self.engine._n_actions

        last_clips = self.engine._total_clips

        # update state
        getattr(self.engine, self.engine.actions[action])()

        reward = self.get_reward(last_clips)

        self.add_to_replay(self.state, action, reward)

        return self.state, reward

    def __call__(self, *args, **kwargs):
        return self.act(*args, **kwargs)
