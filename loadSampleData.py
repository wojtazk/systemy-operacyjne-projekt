from models.Process import Process


def load_cpu_scheduling_sample_data(source_file: str) -> list[Process]:
    processes = []
    with open(source_file, 'r') as file:
        lines = file.readlines()

        for line in lines:
            tmp = line.strip().split(';')
            tmp = [int(x) for x in tmp]
            processes.append(Process(*tmp))

    return processes
