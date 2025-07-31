import minigrid
from minigrid.manual_control import ManualControl
import gymnasium as gym

class ManualControlWithObs(ManualControl):
    def step(self, action):
        print("Action: ",action)
        obs, reward, terminated, truncated, info = self.env.step(action)
        print("Obs:", obs)  # 👈 Aquí se imprime la observación en cada paso
        print("Reward:",reward)
        if terminated or truncated:
            print("Episode done. Resetting environment.")
            self.reset()

# Crear el entorno
env = gym.make("MiniGrid-Empty-16x16-v0", render_mode="human")

# Usar la clase personalizada
manual_control = ManualControlWithObs(env, seed=42)
manual_control.start()

env.close()

#1 es piso
#2 es muro
#8 es meta