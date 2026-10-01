class ReflexAgent2Room:
    def __init__(self):
        # Reflex agent initialization
        # Reflex agents act solely based on the current percept and do not store internal state
        pass

    def __str__(self):
        # Provides a string representation of the reflex agent
        return "Reflex Agent"

    def selectAction(self, percept):
        """
        YOUR CODE GOES HERE
        """
        pass

    def execAction(self, action, environment):
        # Executes the chosen action by modifying the environment's state
        environment.setEnvironment(action)

    def perceiveAndAct(self, environment):
        # This method manages the process of perception and action execution
        # 1. Get the current percept from the environment
        percept = environment.getPerceptFromEnvironment()
        print(f"Perceived: {percept}")  # Output the percept for clarity

        # 2. Select an action based on the percept
        action = self.selectAction(percept)
        print(f"Action selected: {action}")  # Output the selected action

        # 3. Execute the selected action and update the environment's state
        self.execAction(action, environment)
        print(
            f"New Environment state: {environment}"
        )  # Output the updated environment state


class MemoryAgentNRooms:
    def __init__(self):
        # Initialize the memory to store the agent's last two actions
        self.memory = []  # Memory is initially empty

    def __str__(self):
        # Provides a string representation of the memory-based agent
        return "Memory-based Agent"

    def selectAction(self, percept):
        """
        YOUR CODE GOES HERE
        """
        pass

    def execAction(self, action, environment):
        # Executes the chosen action in the environment and updates the agent's memory

        # Update the environment's state based on the action
        environment.setEnvironment(action)

        # Add the action to the agent's memory (store up to the last two actions)
        self.memory.append(action)
        if len(self.memory) > 2:
            self.memory.pop(0)  # Keep only the last two actions in memory

    def perceiveAndAct(self, environment):
        # This method handles the perception and action execution process

        # 1. Get the current percept from the environment
        percept = environment.getPerceptFromEnvironment()
        print(f"Perceived: {percept}")  # Output the percept for clarity

        # 2. Select an action based on the percept and the agent's memory
        action = self.selectAction(percept)
        print(f"Action selected: {action}")  # Output the selected action

        # 3. Execute the selected action and update the environment
        self.execAction(action, environment)
        print(
            f"New Environment state: {environment}"
        )  # Output the updated environment state


class MemoryAgentNXNRooms:
    def __init__(self):
        # Initialize a memory-based agent that stores its last two actions.
        self.memory = []  # Memory starts empty

    def __str__(self):
        # Provide a string representation of the memory-based agent.
        return "Memory-based Agent"

    def selectAction(self, percept):
        """
        YOUR CODE GOES HERE
        """
        pass

    def execAction(self, action, environment):
        # Executes the agent's action and updates the environment accordingly.
        environment.setEnvironment(
            action
        )  # Update the environment based on the chosen action

        # Add the action to the agent's memory, maintaining only the last two actions.
        self.memory.append(action)
        if len(self.memory) > 2:
            self.memory.pop(0)  # Limit memory to the last two actions

    def perceiveAndAct(self, environment):
        # Handle the process of perception and action execution.

        # 1. Get the current percept from the environment.
        percept = environment.getPerceptFromEnvironment()
        print(f"Perceived: {percept}")  # Output the percept for clarity

        # 2. Select an action based on the percept and the agent's memory.
        action = self.selectAction(percept)
        print(f"Action selected: {action}")  # Output the selected action

        # 3. Execute the selected action and update the environment.
        self.execAction(action, environment)
        print(
            f"New Environment state: {environment}"
        )  # Output the updated environment state
