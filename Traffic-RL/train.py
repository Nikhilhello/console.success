from env.traffic_env import TrafficEnv
from agent.dqn_agent import DQNAgent
import numpy as np
import matplotlib.pyplot as plt
import torch

EPISODES = 50
BATCH_SIZE = 32

env = TrafficEnv()
state_size = 8
action_size = 2

agent = DQNAgent(state_size, action_size)

rewards_per_episode = []

for episode in range(EPISODES):
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)

        agent.remember(state, action, reward, next_state, done)
        agent.replay(BATCH_SIZE)

        state = next_state
        total_reward += reward

    rewards_per_episode.append(total_reward)
    print(f"Episode {episode+1}/{EPISODES} | Total Reward: {total_reward:.2f} | Epsilon: {agent.epsilon:.3f}")

# Save model
torch.save(agent.model.state_dict(), "models/traffic_dqn.pth")
print("✅ Model saved as models/traffic_dqn.pth")

# Plot training performance
plt.plot(rewards_per_episode)
plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("DQN Training Performance")
plt.savefig("plots/training_reward.png")
plt.show()
