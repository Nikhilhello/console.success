from static_controller import run_static_controller
from env.traffic_env import TrafficEnv
from agent.dqn_agent import DQNAgent
import torch
import matplotlib.pyplot as plt

env = TrafficEnv()
agent = DQNAgent(8, 2)
agent.model.load_state_dict(torch.load("models/traffic_dqn.pth"))
agent.epsilon = 0  # no exploration

def run_ai():
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.act(state)
        state, reward, done = env.step(action)
        total_reward += reward

    return total_reward

static_rewards = []
ai_rewards = []

for _ in range(10):
    static_rewards.append(run_static_controller())
    ai_rewards.append(run_ai())

plt.plot(static_rewards, label="Static Controller")
plt.plot(ai_rewards, label="AI Controller")
plt.legend()
plt.xlabel("Run")
plt.ylabel("Total Reward")
plt.title("Static vs AI Traffic Control")
plt.savefig("plots/static_vs_ai.png")
plt.show()
