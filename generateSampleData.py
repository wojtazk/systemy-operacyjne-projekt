from uuid import uuid4


# config
NUM_OF_SAMPLES = 10_000
MAX_ARRIVAL_TIME = NUM_OF_SAMPLES ** 2
MAX_BURST_TIME = 5_000

SAMPLE_DATA_DIR = 'simulation_sample_data'
CPU_OUTPUT_FILE = SAMPLE_DATA_DIR + '/' + 'cpu_scheduling_sample_data.txt'


def generate_cpu_scheduling_sample_data() -> None:
    sample_data = []
    for i in range(NUM_OF_SAMPLES):
        arrival_time = int((uuid4().int % MAX_ARRIVAL_TIME) + 1)  # arrival_time in [1, NUM_OF_SAMPLES]
        burst_time = int((uuid4().int % MAX_BURST_TIME) + 1)  # burst_time in [1, MAX_BURST_TIME]
        sample_data.append([arrival_time, burst_time])

    # sort data based on arrival time
    sample_data.sort(key=lambda x: x[0])

    _write_data_to_file(sample_data, CPU_OUTPUT_FILE)


def _write_data_to_file(data: list, filename: str) -> None:
    """Writes data from an array to a file"""
    with open(filename, 'w') as file:
        for sample in data:
            new_line = ';'.join(str(x) for x in sample) + '\n'
            file.write(new_line)
