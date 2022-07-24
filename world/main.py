from game.engine import Engine
from agent.random_agent import RandomAgent


if __name__ == '__main__':
    e = Engine()
    agent = RandomAgent(len(e.actions))

    for i in range(10):
        act = agent.predict(e.state)
        e(act)

    print(e)

