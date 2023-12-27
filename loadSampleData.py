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


def load_page_replacement_sample_data(source_file: str) -> list[int]:
    page_reference_array = []
    with open(source_file, 'r') as file:
        lines = file.readlines()

        for line in lines:
            tmp = int(line.strip())
            page_reference_array.append(tmp)

    return page_reference_array
