from game import EngineRLInterface
from agent import BanditAgent


if __name__ == '__main__':
    e = EngineRLInterface()
    agent = BanditAgent(len(e.actions))

    for i in range(100):
        act = agent.predict(e.state)
        state, reward = e(act)
        agent.update(act, reward)


