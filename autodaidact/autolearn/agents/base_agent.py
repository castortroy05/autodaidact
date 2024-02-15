class BaseAgent:
    """
    A base class for all agents in the AutoDAIdact project. This class defines common 
    interfaces and functionalities for agents, including methods for decision making, 
    learning from interactions, and handling observations from the environment.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseAgent class.
        """
        pass  # Initialize any necessary variables or configurations here

    def select_action(self, state):
        """
        Selects an action to take based on the current state of the environment.

        Parameters:
            state: The current state of the environment.

        Returns:
            An action selected by the agent.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def learn(self, state, action, reward, next_state, done):
        """
        Updates the agent's knowledge based on the most recent interaction with the environment.

        Parameters:
            state: The state before taking the action.
            action: The action taken.
            reward: The reward received for taking the action.
            next_state: The state after taking the action.
            done: A boolean indicating whether the episode has ended.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def reset(self):
        """
        Resets the agent's state at the beginning of a new episode. Useful for agents
        that maintain state or need to reset internal variables between episodes.
        """
        pass  # Implement any necessary reset logic here
