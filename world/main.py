from game.engine import Engine
from game.agent_interface.engine_interface import EngineRLInterface
from agent import BanditAgent, RandomAgent


if __name__ == '__main__':
    e = EngineRLInterface()
    agent = BanditAgent(len(e.actions))

    for i in range(100):
        act = agent.predict(e.state)
        state, reward = e(act)
        agent.update(act, reward)

    print(e.engine)

