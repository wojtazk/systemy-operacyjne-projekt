from models.Process import Process
import copy


def simulate_round_robin(processes: list[Process], time_slice: int) -> list:
    """Simulates a Round-Robin cpu scheduling algorithm"""
    # processes should be sorted by arrival time

    # make local copy of processes array
    processes_copy: list[Process] = copy.deepcopy(processes)
    # set cpu clock to arrival time of first process
    cpu_clock: int = processes_copy[0].arrival_time
    # declare queue array (it queues indexes of processes currently being executed)
    queue: list[int] = [0]
    # initialize variable for storing number of processes in queue
    next_arriving_process_index: int = 1
    # initialize array for storing simulation results
    simulation_results: list = []

    def _add_arriving_processes_to_queue() -> None:
        """Adds processes to queue if their arrival time is less than cpu clock"""
        nonlocal next_arriving_process_index, processes_copy, cpu_clock, queue

        for i in range(next_arriving_process_index, len(processes_copy)):
            p = processes_copy[i]
            if p.arrival_time <= cpu_clock:
                # append pages' index to the queue
                queue.append(i)
                # increase the next arriving process index
                next_arriving_process_index += 1
            else:
                break

    # execute for as long as any task has remaining burst time
    while True:
        # initialize done to True
        # if done is True at the end of the loop, then the simulation is done
        done: bool = True

        # go through processes currently in queue and give each slice of cpu time
        while len(queue) > 0:
            # get first process index from the queue
            current_process_idx = queue[0]
            # get currently executing current_process
            current_process = processes_copy[current_process_idx]

            # if processes still exist in queue -> the algorithm is not done
            # set done to False
            done = False

            # give current_process a slice of cpu time
            # if remaining burst time is more than time slice
            if current_process.remaining_burst_time > time_slice:
                # add time slice to cpu clock
                cpu_clock += time_slice
                # subtract time slice from processes' remaining burst time
                current_process.remaining_burst_time -= time_slice
                # add processes that arrived during execution of the current current_process to the queue
                _add_arriving_processes_to_queue()
                # pop current process' index from the queue
                queue.pop(0)
                # add current process' index at the end of the queue (schedule it for another execution)
                queue.append(current_process_idx)
                # go to the next current_process
                continue

            # if remaining burst time is less than time_slice
            # add remaining burst time to cpu clock
            cpu_clock += current_process.remaining_burst_time
            # set processes' remaining burst time to 0
            current_process.remaining_burst_time = 0
            # set processes' completion time to current cpu clock
            current_process.completion_time = cpu_clock
            # pop the processes' index from queue
            queue.pop(0)

            # calculate processes' turn around time
            current_process.calculate_turn_around_time()
            # calculate processes' waiting time
            current_process.calculate_waiting_time()

            # get processes' properties as list
            tmp = current_process.get_properties_as_list()
            # remove remaining burst time from the list (it would be always 0)
            tmp = tmp[:2] + tmp[3:]  # [arrival_time, burst_time, completion_time, turn_around_time, waiting_time]
            # append properties to the simulation results array
            simulation_results.append(tmp)

            # add arriving processes to the process_queue
            _add_arriving_processes_to_queue()

        # if simulation is done
        if done:
            # break from the while loop
            break

        # if queue is empty and index of next arriving process is less than length of processes_copy array
        if len(queue) == 0 and next_arriving_process_index < len(processes_copy):
            # set cpu_clock to arrival time of the next arriving process
            cpu_clock = processes_copy[next_arriving_process_index].arrival_time
            # append the next arriving process to the queue
            queue.append(next_arriving_process_index)
            # increment the next arriving process index
            next_arriving_process_index += 1

    return simulation_results
