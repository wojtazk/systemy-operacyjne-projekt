from models.Process import Process
import copy


def simulate_fcfs(processes: list[Process]) -> list:
    """Simulates a FCFS cpu scheduling algorithm"""
    processes_copy: list[Process] = copy.deepcopy(processes)
    cpu_clock: int = processes_copy[0].arrival_time
    simulation_results: list = []

    for process in processes_copy:
        if cpu_clock < process.arrival_time:
            cpu_clock = process.arrival_time

        cpu_clock_after_task_execution: int = cpu_clock + process.burst_time
        process.completion_time = cpu_clock_after_task_execution
        cpu_clock = cpu_clock_after_task_execution

        # process.remaining_burst_time = 0  # this is obsolete

        process.calculate_turn_around_time()
        process.calculate_waiting_time()

        tmp = process.get_properties_as_list()
        tmp = tmp[:2] + tmp[3:]  # [arrival_time, burst_time, completion_time, turn_around_time, waiting_time]
        simulation_results.append(tmp)

    return simulation_results
