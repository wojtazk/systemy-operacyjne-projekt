from uuid import uuid4
from helpers import write_data_to_file


def generate_cpu_scheduling_sample_data(num_of_samples: int, max_arrival_time: int, max_burst_time: int,
                                        output_file: str) -> None:
    sample_data = []
    for i in range(num_of_samples):
        arrival_time = (uuid4().int % max_arrival_time) + 1  # arrival_time in [1, num_of_samples]
        burst_time = (uuid4().int % max_burst_time) + 1  # burst_time in [1, max_burst_time]
        sample_data.append([arrival_time, burst_time])

    # sort data based on arrival time
    sample_data.sort(key=lambda x: x[0])

    write_data_to_file(sample_data, output_file)


def generate_page_replacement_sample_data(num_of_samples: int, max_page_reference_num: int, output_file: str) -> None:
    sample_data = []
    for i in range(num_of_samples):
        page_reference_num = uuid4().int % max_page_reference_num
        sample_data.append([page_reference_num])

    write_data_to_file(sample_data, output_file)
