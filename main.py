# noinspection PyUnresolvedReferences
from generateSampleData import generate_cpu_scheduling_sample_data
from loadSampleData import load_cpu_scheduling_sample_data

from cpu_scheduling.FCFS import simulate_fcfs
from cpu_scheduling.Round_Robin import simulate_round_robin

from helpers import write_data_to_file


############################################################################
# config
NUM_OF_SAMPLES = 100_000

MAX_ARRIVAL_TIME = 10_000
MAX_BURST_TIME = 5_000

# CPU_TIME_SLICE = 10
# CPU_TIME_SLICE = 100
CPU_TIME_SLICE = 1000
# CPU_TIME_SLICE = 4000  # basically degrade Round-Robin to FCFS

SIMULATION_SAMPLE_DATA_DIR = 'simulation_sample_data'
SIMULATION_RESULTS_DIR = 'simulation_results'

CPU_SAMPLE_FILE = SIMULATION_SAMPLE_DATA_DIR + '/' + 'cpu_scheduling_sample_data.txt'

CPU_FCFS_RESULTS_FILE = SIMULATION_RESULTS_DIR + '/' + 'FCFS_simulation_results.txt'
CPU_ROUND_ROBIN_RESULTS_FILE = (
        SIMULATION_RESULTS_DIR + '/' + 'Round-Robin_simulation_results_time_slice_' + str(CPU_TIME_SLICE) + '.txt'
)
############################################################################


############################################################################
# CPU scheduling

# generate test data for CPU scheduling algorithms
# generate_cpu_scheduling_sample_data(NUM_OF_SAMPLES, MAX_ARRIVAL_TIME, MAX_BURST_TIME, CPU_SAMPLE_FILE)

# load processes data from file
cpu_scheduling_processes = load_cpu_scheduling_sample_data(CPU_SAMPLE_FILE)

# simulate FCFS and write results to file
fcfs_simulation_data: list = simulate_fcfs(cpu_scheduling_processes)
write_data_to_file(fcfs_simulation_data, CPU_FCFS_RESULTS_FILE)

# simulate Round-Robin and write results to file
round_robin_simulation_data: list = simulate_round_robin(cpu_scheduling_processes, CPU_TIME_SLICE)
write_data_to_file(round_robin_simulation_data, CPU_ROUND_ROBIN_RESULTS_FILE)
############################################################################
