import contextlib
import sys
import io
import time

from src.environments import NxMRoomEnvironment, NRoomEnvironment, Environment2Room
from src.agents import MemoryAgentNXNRooms, MemoryAgentNRooms, ReflexAgent2Room


def run_simulation_2_room():
    # Initialize the environment and the agent
    # The environment is a 2-room setup where both rooms are initially dirty
    # The agent is a reflex agent that makes decisions based on its current percept
    environment = Environment2Room()
    agent = ReflexAgent2Room()

    # Initialize a step counter to track how many actions the agent takes
    steps = 0
    print(
        "Initial state:", environment.state
    )  # Display the initial state of the environment

    # Run the simulation loop until both rooms are clean
    # The loop continues as long as there is dirt ("D") in either room
    while "D" in environment.state[0] or "D" in environment.state[1]:
        print(f"Step {steps}:")  # Display the current step number

        # The agent perceives the current environment and performs an action
        agent.perceiveAndAct(environment)

        # Increment the step counter after each action
        steps += 1

    # Once the loop ends, the environment is clean
    print(
        "The environment is now clean!"
    )  # Output a message indicating the simulation is complete


def run_simulation_n_rooms(n):
    # Initialize the environment and the agent
    # The environment is an n-room setup, where all rooms start dirty, and the agent is placed randomly in one of them
    environment = NRoomEnvironment(n)
    agent = (
        MemoryAgentNRooms()
    )  # The agent uses memory to decide its actions based on previous steps

    # Initialize a step counter to track how many actions the agent takes
    steps = 0
    print(
        "Initial state:", environment.state
    )  # Display the initial state of the environment

    # Run the simulation until all rooms are clean
    # The loop continues as long as any room contains dirt ("D")
    while any("D" in room for room in environment.state):
        print(f"Step {steps}:")  # Display the current step number

        # The agent perceives the current environment state and performs an action
        agent.perceiveAndAct(environment)

        # Increment the step counter after each action
        steps += 1

    # Once the loop ends, all rooms are clean
    print(
        "The environment is now clean!"
    )  # Output a message indicating the simulation is complete
    print(
        f"Total steps: {steps}"
    )  # Output the total number of steps taken to clean all rooms
    print(
        "================================================"
    )  # Separator for clarity when running multiple tests


# Function to run the simulation for an n x m grid of rooms
def run_simulation_nxm_rooms(n, m):
    # Initialize the environment and the agent
    # The environment is an n x m grid where each room is initially dirty, and the agent is placed in a random room
    environment = NxMRoomEnvironment(n, m)
    agent = MemoryAgentNXNRooms()  # The agent uses memory to track its last actions

    # Initialize a step counter to track how many actions the agent takes
    steps = 0
    print(
        "Initial state:", environment.state
    )  # Display the initial state of the environment

    # Run the simulation until all rooms in the grid are clean
    # The loop continues as long as any room in the environment still contains dirt ("D")
    while any("D" in room for row in environment.state for room in row):
        print(f"Step {steps}:")  # Display the current step number

        # The agent perceives the environment and performs an action
        agent.perceiveAndAct(environment)

        # Increment the step counter after each action
        steps += 1

    # Once all rooms are clean, the loop ends
    print(
        "The environment is now clean!"
    )  # Output a message indicating the environment is fully cleaned
    print(
        f"Total steps: {steps}"
    )  # Output the total number of steps taken by the agent
    print(
        f"=================================================="
    )  # Separator for clarity between different test runs


# TEST VERSIONS WITHOUT PRINTS - For automated testing


@contextlib.contextmanager
def suppress_all_prints():
    """Context manager to suppress all prints by replacing the print function"""
    # Save original print function
    original_print = print

    # Replace print with a no-op function
    import builtins

    builtins.print = lambda *args, **kwargs: None

    # Also redirect stdout/stderr as backup
    old_stdout = sys.stdout
    old_stderr = sys.stderr

    try:
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
        yield
    finally:
        # Restore everything
        builtins.print = original_print
        sys.stdout = old_stdout
        sys.stderr = old_stderr


def run_simulation_2_room_test(max_steps=None):
    """Lightweight silent version of 2-room simulation for testing"""
    environment = Environment2Room()
    agent = ReflexAgent2Room()

    if max_steps is None:
        max_steps = 2 * 10  # small safety cap

    steps = 0
    with suppress_all_prints():
        while "D" in environment.state[0] or "D" in environment.state[1]:
            agent.perceiveAndAct(environment)
            steps += 1
            if steps >= max_steps:
                time.sleep(2)

    return steps


def run_simulation_n_rooms_test(n, max_steps=None):
    """Lightweight silent version of n-room simulation for testing"""
    environment = NRoomEnvironment(n)
    agent = MemoryAgentNRooms()

    if max_steps is None:
        max_steps = n * 100  # safety cap

    steps = 0
    with suppress_all_prints():
        while any("D" in room for room in environment.state):
            agent.perceiveAndAct(environment)
            steps += 1
            if steps >= max_steps:
                time.sleep(2)

    return steps


def run_simulation_nxm_rooms_test(n, m, max_steps=None):
    """Lightweight silent version of nxm-room simulation for testing"""
    environment = NxMRoomEnvironment(n, m)
    agent = MemoryAgentNXNRooms()

    if max_steps is None:
        max_steps = n * m * 100  # safety cap

    steps = 0
    with suppress_all_prints():
        while any("D" in room for row in environment.state for room in row):
            agent.perceiveAndAct(environment)
            steps += 1
            if steps >= max_steps:
                time.sleep(2)

    return steps
