from models.Process import Process
import copy


def simulate_fcfs(processes: list[Process]) -> list:
    """Simulates a FCFS cpu scheduling algorithm"""

    # make local copy of processes array
    processes_copy: list[Process] = copy.deepcopy(processes)
    # set cpu clock to the first arriving task
    cpu_clock: int = processes_copy[0].arrival_time
    # initialize array for storing simulation results
    simulation_results: list = []

    for current_process in processes_copy:
        # if cpu clock is less than processes' arrival time
        if cpu_clock < current_process.arrival_time:
            # set cpu clock to processes' arrival time
            cpu_clock = current_process.arrival_time

        # increase cpu clock by processes' burst time
        cpu_clock += current_process.burst_time
        # assign processes' completion time
        current_process.completion_time = cpu_clock

        # current_process.remaining_burst_time = 0  # this is obsolete

        # calculate processes' turn around time
        current_process.calculate_turn_around_time()
        # calculate processes' waiting time
        current_process.calculate_waiting_time()

        # get processes' properties and append them to simulation results array
        tmp = current_process.get_properties_as_list()
        tmp = tmp[:2] + tmp[3:]  # [arrival_time, burst_time, completion_time, turn_around_time, waiting_time]
        simulation_results.append(tmp)

    return simulation_results
