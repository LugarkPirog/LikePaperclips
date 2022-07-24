from abc import ABC


class BaseAgent(ABC):
    def __init__(self, n_actions):
        self.actions = list(range(n_actions))

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def predict(self, *args, **kwargs):
        return self(*args, **kwargs)
