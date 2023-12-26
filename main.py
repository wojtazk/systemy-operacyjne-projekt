# noinspection PyUnresolvedReferences
from generateSampleData import generate_cpu_scheduling_sample_data
from loadSampleData import load_cpu_scheduling_sample_data


############################################################################
# config
NUM_OF_SAMPLES = 10_000
MAX_ARRIVAL_TIME = NUM_OF_SAMPLES ** 2
MAX_BURST_TIME = 5_000

SIMULATION_SAMPLE_DATA_DIR = 'simulation_sample_data'
SIMULATION_RESULTS_DIR = 'simulation_results'

CPU_SAMPLE_FILE = SIMULATION_SAMPLE_DATA_DIR + '/' + 'cpu_scheduling_sample_data.txt'

CPU_FCFS_RESULTS_FILE = 'FCFS_simulation_results.txt'
CPU_ROUND_ROBIN_RESULTS_FILE = 'Round-Robin_simulation_results.txt'
############################################################################


# generate test data for CPU scheduling algorithms
# FIXME: uncomment to generate new cpu scheduling sample data
# generate_cpu_scheduling_sample_data(NUM_OF_SAMPLES, MAX_ARRIVAL_TIME, MAX_BURST_TIME, CPU_SAMPLE_FILE)

cpu_scheduling_processes = load_cpu_scheduling_sample_data(CPU_SAMPLE_FILE)
print()
