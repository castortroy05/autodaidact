import gym

class AutoLearnEnv:
    def __init__(self):
        self.env = gym.make('CartPole-v1')
        self.state = self.env.reset()

    def run_episode(self, steps=1000):
        for _ in range(steps):
            self.env.render()
            action = self.env.action_space.sample()  # This will be replaced with a smarter decision in the future
            state, reward, done, info = self.env.step(action)
            if done:
                self.env.reset()

    def close(self):
        self.env.close()

def main_menu():
    env = AutoLearnEnv()
    while True:
        print("\nAutoLearnAI Main Menu")
        print("1. Start Environment")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                env.run_episode()
            finally:
                env.close()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()
