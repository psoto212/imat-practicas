import pytest
import multiprocessing
import time
import sys
import os

# Add the project root directory to Python path (works on any machine)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)  # Go up from tests/ to project root
sys.path.insert(0, project_root)

from src.simulations import (
    run_simulation_2_room_test,
    run_simulation_n_rooms_test,
    run_simulation_nxm_rooms_test,
)


def run_2room_simulation(result_queue):
    """Module-level function for 2-room simulation"""
    try:
        steps = run_simulation_2_room_test()
        result_queue.put({"completed": True, "steps": steps, "exception": None})
    except Exception as e:
        result_queue.put({"completed": False, "steps": 0, "exception": str(e)})


def run_nroom_simulation(n, result_queue):
    """Module-level function for n-room simulation"""
    try:
        steps = run_simulation_n_rooms_test(n)
        result_queue.put({"completed": True, "steps": steps, "exception": None})
    except Exception as e:
        result_queue.put({"completed": False, "steps": 0, "exception": str(e)})


def run_nxm_simulation(n, m, result_queue):
    """Module-level function for nxm-room simulation"""
    try:
        steps = run_simulation_nxm_rooms_test(n, m)
        result_queue.put({"completed": True, "steps": steps, "exception": None})
    except Exception as e:
        result_queue.put({"completed": False, "steps": 0, "exception": str(e)})


def test_2room_simulation_timeout():
    """Test that 2-room simulation completes within 1 second"""
    result_queue = multiprocessing.Queue()

    process = multiprocessing.Process(target=run_2room_simulation, args=(result_queue,))
    start_time = time.time()
    process.start()

    # Wait for 1 second
    process.join(timeout=1.0)

    if process.is_alive():
        # Force kill the process if it's still running
        process.terminate()
        process.join()  # Wait for termination to complete
        pytest.fail("2-room simulation did not complete within 1 second")

    # Check if there's a result
    if not result_queue.empty():
        result = result_queue.get()

        if result["exception"]:
            pytest.fail(f"Simulation failed with exception: {result['exception']}")

        if result["completed"]:
            elapsed_time = time.time() - start_time
            print(
                f"2-room simulation completed in {elapsed_time:.3f} seconds with {result['steps']} steps"
            )
    else:
        pytest.fail("2-room simulation produced no result")


def test_nroom_simulation_timeout():
    """Test that 5-room simulation completes within 1 second"""
    result_queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=run_nroom_simulation, args=(5, result_queue)
    )
    start_time = time.time()
    process.start()

    process.join(timeout=1.0)

    if process.is_alive():
        process.terminate()
        process.join()
        pytest.fail("5-room simulation did not complete within 1 second")

    if not result_queue.empty():
        result = result_queue.get()

        if result["exception"]:
            pytest.fail(f"Simulation failed with exception: {result['exception']}")

        if result["completed"]:
            elapsed_time = time.time() - start_time
            print(
                f"5-room simulation completed in {elapsed_time:.3f} seconds with {result['steps']} steps"
            )
    else:
        pytest.fail("5-room simulation produced no result")


def test_nxm_room_simulation_timeout():
    """Test that 3x3 room simulation completes within 1 second"""
    result_queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=run_nxm_simulation, args=(3, 3, result_queue)
    )
    start_time = time.time()
    process.start()

    process.join(timeout=1.0)

    if process.is_alive():
        process.terminate()
        process.join()
        pytest.fail("3x3 room simulation did not complete within 1 second")

    if not result_queue.empty():
        result = result_queue.get()

        if result["exception"]:
            pytest.fail(f"Simulation failed with exception: {result['exception']}")

        if result["completed"]:
            elapsed_time = time.time() - start_time
            print(
                f"3x3 room simulation completed in {elapsed_time:.3f} seconds with {result['steps']} steps"
            )
    else:
        pytest.fail("3x3 room simulation produced no result")


if __name__ == "__main__":
    # This is needed for Windows multiprocessing
    multiprocessing.freeze_support()
