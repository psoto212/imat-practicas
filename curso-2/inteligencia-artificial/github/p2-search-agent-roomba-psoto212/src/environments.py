import random


class Environment2Room:
    def __init__(self):
        # Initial state of the environment: a list of two rooms
        # The left room contains both the agent and dirt ("AD"), and the right room contains only dirt ("D")
        # "A" represents the agent, "D" represents dirt, and an empty string represents a clean room with no agent
        self.state = ["AD", "D"]  # Agent starts in the left room, both rooms are dirty

    def __str__(self):
        # Provides a string representation of the current state of the environment
        return f"Environment state: {self.state}"

    def getPerceptFromEnvironment(self):
        # Generates a percept for the agent to act upon
        # The percept is a dictionary containing the agent's location and whether the current room is dirty

        percept = {}  # Initialize an empty dictionary to store percepts

        # Check if the agent is in the left room
        if "A" in self.state[0]:
            percept["agent_location"] = "L"  # Agent is in the left room
            percept["dirty"] = "D" in self.state[0]  # Check if the left room is dirty
        # Check if the agent is in the right room
        elif "A" in self.state[1]:
            percept["agent_location"] = "R"  # Agent is in the right room
            percept["dirty"] = "D" in self.state[1]  # Check if the right room is dirty

        return percept  # Return the percept for the agent to use

    def setEnvironment(self, action):
        # This method updates the environment's state based on the agent's action
        # It supports cleaning the current room or moving between rooms

        # Determine which room the agent is in (left or right)
        agent_location = "L" if "A" in self.state[0] else "R"

        if action == "clean":
            # If the action is "clean", remove the dirt from the current room
            if agent_location == "L":
                self.state[0] = self.state[0].replace("D", "")  # Clean the left room
            else:
                self.state[1] = self.state[1].replace("D", "")  # Clean the right room

        elif action == "moveR" and agent_location == "L":
            # If the action is "moveR", move the agent from the left room to the right room
            self.state[0] = self.state[0].replace(
                "A", ""
            )  # Remove agent from the left room
            self.state[1] = "A" + self.state[1]  # Add agent to the right room

        elif action == "moveL" and agent_location == "R":
            # If the action is "moveL", move the agent from the right room to the left room
            self.state[1] = self.state[1].replace(
                "A", ""
            )  # Remove agent from the right room
            self.state[0] = "A" + self.state[0]  # Add agent to the left room


class NRoomEnvironment:
    def __init__(self, n):
        # Initialize an environment with 'n' rooms. All rooms are initially dirty.
        # Place the agent in a random room. The agent's position is chosen randomly from the available rooms.
        agent_position = random.randint(
            0, n - 1
        )  # Randomly select a room for the agent
        self.state = ["D"] * n  # Initialize all rooms as dirty (represented by "D")
        self.state[agent_position] = (
            "AD"  # Place agent in the randomly selected room and mark it dirty
        )
        self.n = n  # Store the number of rooms in the environment

    def __str__(self):
        # Provides a string representation of the current environment state
        return f"Environment state: {self.state}"

    def getPerceptFromEnvironment(self):
        # Generate the agent's percept from the current state of the environment
        percept = {}

        # Identify the agent's location by finding which room contains "A"
        agent_location = next(i for i, room in enumerate(self.state) if "A" in room)

        percept["dirty"] = (
            "D" in self.state[agent_location]
        )  # Check if the current room is dirty

        # Check if the agent is in the leftmost or rightmost room (adjacent to a wall)
        percept["wall"] = agent_location == 0 or agent_location == self.n - 1

        return percept  # Return the percept for the agent to use

    def setEnvironment(self, action):
        # Update the environment's state based on the agent's chosen action

        # Find the current location of the agent
        agent_location = next(i for i, room in enumerate(self.state) if "A" in room)

        if action == "clean":
            # Clean the current room (remove "D" from the room's state)
            self.state[agent_location] = self.state[agent_location].replace("D", "")

        elif action == "moveR" and agent_location < self.n - 1:
            # Move the agent to the right if not in the rightmost room
            self.state[agent_location] = self.state[agent_location].replace(
                "A", ""
            )  # Remove agent from the current room
            self.state[agent_location + 1] = (
                "A" + self.state[agent_location + 1]
            )  # Place agent in the next room to the right

        elif action == "moveL" and agent_location > 0:
            # Move the agent to the left if not in the leftmost room
            self.state[agent_location] = self.state[agent_location].replace(
                "A", ""
            )  # Remove agent from the current room
            self.state[agent_location - 1] = (
                "A" + self.state[agent_location - 1]
            )  # Place agent in the next room to the left


class NxMRoomEnvironment:
    def __init__(self, n, m):
        # Initialize an n x m grid environment where all rooms are initially dirty.
        self.n = n  # Number of rows
        self.m = m  # Number of columns

        # Create a grid where each room is marked as dirty (represented by "D").
        self.state = [["D" for _ in range(m)] for _ in range(n)]

        # Randomly place the agent in one of the rooms, ensuring the agent is placed within the grid.
        self.agent_position = [
            random.randint(1, n - 1),
            random.randint(1, m - 1),
        ]  # Random position for agent
        self.state[self.agent_position[0]][
            self.agent_position[1]
        ] = "AD"  # Place agent in the randomly selected room

    def __str__(self):
        # Provide a human-readable string representation of the environment grid.
        grid = "\n".join(
            [" ".join(row) for row in self.state]
        )  # Format the grid into rows for printing
        return f"Environment state:\n{grid}"  # Return the formatted grid

    def getPerceptFromEnvironment(self):
        # Generate the agent's percept based on its current state in the environment.
        percept = {}

        # Identify the agent's current location in the grid.
        x, y = self.agent_position

        percept["dirty"] = "D" in self.state[x][y]  # Check if the current room is dirty

        # Check if the agent is adjacent to any walls (left, right, upper, or lower boundary).
        walls = []
        if y == 0:
            walls.append("L")  # Left wall
        if y == self.m - 1:
            walls.append("R")  # Right wall
        if x == 0:
            walls.append("U")  # Upper wall
        if x == self.n - 1:
            walls.append("D")  # Bottom wall

        percept["walls"] = walls  # Store the walls percept (if any)

        return percept  # Return the percept for the agent to use

    def setEnvironment(self, action):
        # Update the environment based on the agent's chosen action.

        # Find the current location of the agent.
        x, y = self.agent_position

        if action == "clean":
            # Clean the current room by removing "D" (dirt).
            self.state[x][y] = self.state[x][y].replace("D", "")

        elif action == "moveR" and y < self.m - 1:
            # Move the agent one room to the right, if not at the rightmost edge.
            self.state[x][y] = self.state[x][y].replace(
                "A", ""
            )  # Remove agent from current room
            self.agent_position = [x, y + 1]  # Update agent position
            self.state[x][y + 1] = (
                "A" + self.state[x][y + 1]
            )  # Add agent to the new room

        elif action == "moveL" and y > 0:
            # Move the agent one room to the left, if not at the leftmost edge.
            self.state[x][y] = self.state[x][y].replace(
                "A", ""
            )  # Remove agent from current room
            self.agent_position = [x, y - 1]  # Update agent position
            self.state[x][y - 1] = (
                "A" + self.state[x][y - 1]
            )  # Add agent to the new room

        elif action == "moveU" and x > 0:
            # Move the agent one room up, if not at the topmost edge.
            self.state[x][y] = self.state[x][y].replace(
                "A", ""
            )  # Remove agent from current room
            self.agent_position = [x - 1, y]  # Update agent position
            self.state[x - 1][y] = (
                "A" + self.state[x - 1][y]
            )  # Add agent to the new room

        elif action == "moveD" and x < self.n - 1:
            # Move the agent one room down, if not at the bottommost edge.
            self.state[x][y] = self.state[x][y].replace(
                "A", ""
            )  # Remove agent from current room
            self.agent_position = [x + 1, y]  # Update agent position
            self.state[x + 1][y] = (
                "A" + self.state[x + 1][y]
            )  # Add agent to the new room
