"""Shared, dependency-light reinforcement-learning helpers."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

LAB_DIR = Path(__file__).parent
OUTPUT_DIR = LAB_DIR / "outputs"

class GridWorld:
    """Small deterministic 4x4 environment with a terminal goal."""
    def __init__(self, size=4):
        self.size = size
        self.start = 0
        self.goal = size * size - 1
        self.state = self.start
        self.n_states = size * size
        self.n_actions = 4

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        row, col = divmod(self.state, self.size)
        if action == 0: row = max(0, row - 1)
        elif action == 1: row = min(self.size - 1, row + 1)
        elif action == 2: col = max(0, col - 1)
        else: col = min(self.size - 1, col + 1)
        self.state = row * self.size + col
        done = self.state == self.goal
        return self.state, (10.0 if done else -1.0), done

def choose_action(table, state, epsilon, rng):
    if rng.random() < epsilon:
        return int(rng.integers(table.shape[1]))
    return int(np.argmax(table[state]))

def train(episodes=300, alpha=.1, gamma=.95, epsilon=.2, seed=42):
    env, rng = GridWorld(), np.random.default_rng(seed)
    q_table = np.zeros((env.n_states, env.n_actions))
    rewards = []
    for _ in range(episodes):
        state, total = env.reset(), 0.0
        for _ in range(100):
            action = choose_action(q_table, state, epsilon, rng)
            next_state, reward, done = env.step(action)
            q_table[state, action] += alpha * (reward + gamma * np.max(q_table[next_state]) * (not done) - q_table[state, action])
            state, total = next_state, total + reward
            if done: break
        rewards.append(total)
    return env, q_table, np.array(rewards)

def plot_rewards(rewards, name):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.plot(rewards); plt.xlabel('Episode'); plt.ylabel('Reward'); plt.tight_layout()
    path = OUTPUT_DIR / name; plt.savefig(path, dpi=140); plt.close(); return path

def greedy_path(table):
    env, state, path = GridWorld(), 0, [0]
    for _ in range(30):
        state, _, done = env.step(int(np.argmax(table[state]))); path.append(state)
        if done: break
    return path
