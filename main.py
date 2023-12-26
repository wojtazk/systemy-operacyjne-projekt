# noinspection PyUnresolvedReferences
from generateSampleData import generate_cpu_scheduling_sample_data
from loadSampleData import load_cpu_scheduling_sample_data

from cpu_scheduling.FCFS import simulate_fcfs

from helpers import write_data_to_file


############################################################################
# config
NUM_OF_SAMPLES = 100_000
MAX_ARRIVAL_TIME = 10_000
MAX_BURST_TIME = 5_000

SIMULATION_SAMPLE_DATA_DIR = 'simulation_sample_data'
SIMULATION_RESULTS_DIR = 'simulation_results'

CPU_SAMPLE_FILE = SIMULATION_SAMPLE_DATA_DIR + '/' + 'cpu_scheduling_sample_data.txt'

CPU_FCFS_RESULTS_FILE = SIMULATION_RESULTS_DIR + '/' + 'FCFS_simulation_results.txt'
CPU_ROUND_ROBIN_RESULTS_FILE = SIMULATION_RESULTS_DIR + '/' + 'Round-Robin_simulation_results.txt'
############################################################################


############################################################################
# CPU scheduling

# generate test data for CPU scheduling algorithms
# FIXME: uncomment to generate new cpu scheduling sample data
# generate_cpu_scheduling_sample_data(NUM_OF_SAMPLES, MAX_ARRIVAL_TIME, MAX_BURST_TIME, CPU_SAMPLE_FILE)

cpu_scheduling_processes = load_cpu_scheduling_sample_data(CPU_SAMPLE_FILE)

fcfs_simulation_data: list = simulate_fcfs(cpu_scheduling_processes)
write_data_to_file(fcfs_simulation_data, CPU_FCFS_RESULTS_FILE)
############################################################################
