from models.Process import Process
import copy


def simulate_round_robin(processes: list[Process], time_slice: int) -> list:
    """Simulates a Round-Robin cpu scheduling algorithm"""
    processes_copy: list[Process] = copy.deepcopy(processes)
    num_of_processes_in_queue: int = 0
    cpu_clock: int = processes_copy[0].arrival_time
    simulation_results: list = []

    while True:
        done: bool = True

        # add arriving processes to the process_queue
        for i in range(num_of_processes_in_queue, len(processes_copy)):
            process = processes_copy[i]
            if process.arrival_time <= cpu_clock:
                num_of_processes_in_queue += 1
            else:
                break

        for i in range(num_of_processes_in_queue):
            process = processes_copy[i]

            # continue if process is already finished
            if process.remaining_burst_time == 0:
                continue

            # if tasks with remaining burst time still exist -> the algorithm is not done
            done = False

            # give process a slice of cpu time
            # remaining burst time is more than time_slice
            if process.remaining_burst_time > time_slice:
                cpu_clock += time_slice
                process.remaining_burst_time -= time_slice
                continue

            # remaining burst time is less than time_slice
            cpu_clock += process.remaining_burst_time
            process.remaining_burst_time = 0
            process.completion_time = cpu_clock

            process.calculate_turn_around_time()
            process.calculate_waiting_time()

            tmp = process.get_properties_as_list()
            tmp = tmp[:2] + tmp[3:]  # [arrival_time, burst_time, completion_time, turn_around_time, waiting_time]
            simulation_results.append(tmp)

        if done:
            break

    return simulation_results
