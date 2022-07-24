import numpy as np

from .base_agent import BaseAgent


class BanditAgent(BaseAgent):
    def __init__(self, n_actions, _type='egreedy', eps=1e-1, lmbda=2e-1):
        super().__init__(n_actions)
        assert _type in ('egreedy', 'softmax'), 'Only greedy and softmax strategies implemented rn'
        self._type = _type

        self.eps = eps
        self.lmbda = lmbda
        self._result_dict = {k:dict(total=0, success=0) for k in self.actions}
        self.probs = np.ones(n_actions) / n_actions

    def egreedy(self):
        if np.random.rand() < self.eps:
            return np.random.choice(self.actions)
        else:
            return np.argmax(self.probs)

    def softmax(self):
        return np.random.choice(self.actions, p=self.probs)

    def __call__(self, *args, **kwargs):
        return getattr(self, self._type)()

    def update(self, action, reward):
        assert reward in (0, 1), 'This guy accepts only 0 or 1 as a reward'
        self._result_dict[action]['total'] += 1
        self._result_dict[action]['success'] += reward

        new_probs = np.array([self._result_dict[k]['success'] / (1+self._result_dict[k]['total']) for k in self._result_dict])
        self.probs = (1-self.lmbda) * self.probs + self.lmbda * new_probs
        self.probs = self.probs / self.probs.sum()
