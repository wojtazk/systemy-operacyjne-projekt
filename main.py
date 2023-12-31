# noinspection PyUnresolvedReferences
from generateSampleData import generate_cpu_scheduling_sample_data
# noinspection PyUnresolvedReferences
from generateSampleData import generate_page_replacement_sample_data

from loadSampleData import load_cpu_scheduling_sample_data
from loadSampleData import load_page_replacement_sample_data

from cpu_scheduling.FCFS import simulate_fcfs
from cpu_scheduling.Round_Robin import simulate_round_robin

from page_replacement.FIFO import simulate_fifo_page_replacement
from page_replacement.LFU import simulate_lfu_page_replacement

from helpers import write_data_to_file

from datetime import datetime

############################################################################
# config
NUM_OF_SAMPLES = 100_000

# cpu scheduling
MAX_ARRIVAL_TIME = 10_000
MAX_BURST_TIME = 5_000
# CPU_TIME_SLICE = 10
# CPU_TIME_SLICE = 100
CPU_TIME_SLICE = 1000
# CPU_TIME_SLICE = 4000  # basically degrade Round-Robin to FCFS

# page replacement
PAGE_MEMORY_CAPACITY = 1000  # number of pages that can fit into the memory
# PAGE_MEMORY_CAPACITY = 2000
# PAGE_MEMORY_CAPACITY = 5000
# PAGE_MEMORY_CAPACITY = 10_000
MAX_PAGE_REFERENCE_NUM = 10_000


SAMPLE_DATA_DIR = 'simulation_sample_data'
RESULTS_DIR = 'simulation_results'

CPU_SAMPLE_FILE = f'{SAMPLE_DATA_DIR}/cpu_scheduling_sample_data.txt'
PAGE_SAMPLE_FILE = (
    f'{SAMPLE_DATA_DIR}/page_replacement_sample_data.txt'
)

CPU_FCFS_RESULTS_FILE = f'{RESULTS_DIR}/FCFS_simulation_results.txt'
CPU_ROUND_ROBIN_RESULTS_FILE = (
    f'{RESULTS_DIR}/Round-Robin_simulation_results_time_slice_{str(CPU_TIME_SLICE)}.txt'
)

PAGE_FIFO_RESULTS_FILE = (
    f'{RESULTS_DIR}/FIFO_simulation_results_page_frames_{str(PAGE_MEMORY_CAPACITY)}.txt'
)
PAGE_LFU_RESULTS_FILE = (
    f'{RESULTS_DIR}/LFU_simulation_results_page_frames_{str(PAGE_MEMORY_CAPACITY)}.txt'
)
############################################################################


############################################################################
# CPU scheduling
# get current time
cpu_sim_start = datetime.now()

# generate test data for CPU scheduling algorithms
# FIXME: uncomment to generate new cpu sample data
# generate_cpu_scheduling_sample_data(NUM_OF_SAMPLES, MAX_ARRIVAL_TIME, MAX_BURST_TIME, CPU_SAMPLE_FILE)

# load processes data from file
cpu_scheduling_processes = load_cpu_scheduling_sample_data(CPU_SAMPLE_FILE)

# simulate FCFS and write results to file
fcfs_simulation_data: list = simulate_fcfs(cpu_scheduling_processes)
write_data_to_file(fcfs_simulation_data, CPU_FCFS_RESULTS_FILE)

# simulate Round-Robin and write results to file
round_robin_simulation_data: list = simulate_round_robin(cpu_scheduling_processes, CPU_TIME_SLICE)
write_data_to_file(round_robin_simulation_data, CPU_ROUND_ROBIN_RESULTS_FILE)

# print how much execution took
print(f'cpu scheduling simulation took: {(datetime.now() - cpu_sim_start).total_seconds()} sec')
############################################################################


############################################################################
# page replacement
# get current time
page_sim_start = datetime.now()

# generate page replacement sample data
# FIXME: uncomment to generate new page replacement sample data
# generate_page_replacement_sample_data(NUM_OF_SAMPLES, MAX_PAGE_REFERENCE_NUM, PAGE_SAMPLE_FILE)

# load page references from file
page_reference_array = load_page_replacement_sample_data(PAGE_SAMPLE_FILE)

# simulate fifo page replacement and write results to file
fifo_simulation_data: list = (
    simulate_fifo_page_replacement(page_reference_array, PAGE_MEMORY_CAPACITY, MAX_PAGE_REFERENCE_NUM)
)
write_data_to_file(fifo_simulation_data, PAGE_FIFO_RESULTS_FILE)

# simulate LFU page replacement and write results to file
lfu_simulation_data: list = (
    simulate_lfu_page_replacement(page_reference_array, PAGE_MEMORY_CAPACITY, MAX_PAGE_REFERENCE_NUM)
)
write_data_to_file(lfu_simulation_data, PAGE_LFU_RESULTS_FILE)

# print how much execution took
print(f'page replacement simulation took: {(datetime.now() - page_sim_start).total_seconds()} sec')
############################################################################
