from env.traffic_env import TrafficEnv

def run_static_controller():
    env = TrafficEnv()
    state = env.reset()
    total_reward = 0
    done = False
    step = 0

    while not done:
        action = step % 2  # fixed switching
        _, reward, done = env.step(action)
        total_reward += reward
        step += 1

    return total_reward

if __name__ == "__main__":
    reward = run_static_controller()
    print("Static Controller Total Reward:", reward)
