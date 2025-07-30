import minigrid  
import gymnasium as gym

env = gym.make("MiniGrid-Empty-8x8-v0", render_mode="human")
obs, _ = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    print(obs)
    done = terminated or truncated

env.close()
