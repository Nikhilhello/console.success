<<<<<<< HEAD
import numpy as np
import random

class TrafficEnv:
    def __init__(self):
        # Cars in each lane
        self.lanes = {
            "N": 0,
            "S": 0,
            "E": 0,
            "W": 0
        }

        # Waiting time in each lane
        self.wait_time = {
            "N": 0,
            "S": 0,
            "E": 0,
            "W": 0
        }

        # 0 = NS Green, 1 = EW Green
        self.light = 0
        self.time_step = 0

    def reset(self):
        for lane in self.lanes:
            self.lanes[lane] = random.randint(0, 5)
            self.wait_time[lane] = 0

        self.light = 0
        self.time_step = 0

        return self.get_state()

    def get_state(self):
        state = [
            self.lanes["N"],
            self.lanes["S"],
            self.lanes["E"],
            self.lanes["W"],
            self.wait_time["N"],
            self.wait_time["S"],
            self.wait_time["E"],
            self.wait_time["W"]
        ]
        return np.array(state, dtype=np.float32)

    def step(self, action):
        reward = 0

        # Ambulance detection (simulated)
        ambulance_lane = random.choice([None, "N", "S", "E", "W"])

        if ambulance_lane:
            # Override signal for ambulance
            if ambulance_lane in ["N", "S"]:
                self.light = 0
            else:
                self.light = 1
        else:
            # Normal RL decision
            self.light = action


        ##-----
        # Cars pass if green
        if self.light == 0:  # NS Green
            passed = min(2, self.lanes["N"])
            self.lanes["N"] -= passed

            passed = min(2, self.lanes["S"])
            self.lanes["S"] -= passed
        else:  # EW Green
            passed = min(2, self.lanes["E"])
            self.lanes["E"] -= passed

            passed = min(2, self.lanes["W"])
            self.lanes["W"] -= passed

        # Add new arriving cars
        for lane in self.lanes:
            self.lanes[lane] += random.randint(0, 2)

        # Update waiting time and reward
        for lane in self.lanes:
            self.wait_time[lane] += self.lanes[lane]
            reward -= self.lanes[lane]

        self.time_step += 1
        done = self.time_step >= 50

        return self.get_state(), reward, done

=======
import numpy as np
import random

class TrafficEnv:
    def __init__(self):
        # Cars in each lane
        self.lanes = {
            "N": 0,
            "S": 0,
            "E": 0,
            "W": 0
        }

        # Waiting time in each lane
        self.wait_time = {
            "N": 0,
            "S": 0,
            "E": 0,
            "W": 0
        }

        # 0 = NS Green, 1 = EW Green
        self.light = 0
        self.time_step = 0

    def reset(self):
        for lane in self.lanes:
            self.lanes[lane] = random.randint(0, 5)
            self.wait_time[lane] = 0

        self.light = 0
        self.time_step = 0

        return self.get_state()

    def get_state(self):
        state = [
            self.lanes["N"],
            self.lanes["S"],
            self.lanes["E"],
            self.lanes["W"],
            self.wait_time["N"],
            self.wait_time["S"],
            self.wait_time["E"],
            self.wait_time["W"]
        ]
        return np.array(state, dtype=np.float32)

    def step(self, action):
        reward = 0

        # Ambulance detection (simulated)
        ambulance_lane = random.choice([None, "N", "S", "E", "W"])

        if ambulance_lane:
            # Override signal for ambulance
            if ambulance_lane in ["N", "S"]:
                self.light = 0
            else:
                self.light = 1
        else:
            # Normal RL decision
            self.light = action


        ##-----
        # Cars pass if green
        if self.light == 0:  # NS Green
            passed = min(2, self.lanes["N"])
            self.lanes["N"] -= passed

            passed = min(2, self.lanes["S"])
            self.lanes["S"] -= passed
        else:  # EW Green
            passed = min(2, self.lanes["E"])
            self.lanes["E"] -= passed

            passed = min(2, self.lanes["W"])
            self.lanes["W"] -= passed

        # Add new arriving cars
        for lane in self.lanes:
            self.lanes[lane] += random.randint(0, 2)

        # Update waiting time and reward
        for lane in self.lanes:
            self.wait_time[lane] += self.lanes[lane]
            reward -= self.lanes[lane]

        self.time_step += 1
        done = self.time_step >= 50

        return self.get_state(), reward, done

>>>>>>> 573c7ac23a17814879212c5f51e4addbb4ecd1f0
