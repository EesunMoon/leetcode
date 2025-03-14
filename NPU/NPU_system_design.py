import numpy as np
import time

"""
    0. Define precision / NPU parameters
        precision: FP16 or INT8
        NPU
    1. Compute-unit: Systolic Array
    2. Memory-unit
    3. Data controller
    4. NPU simulation
"""

# 0) Define parameter
PRECISION = 8                  # FP16, INT8

PE_SIZE = 8                     # Number of systolic array cores
TILE_SIZE = 16                  # 16 x 16 tiling
ON_CHIP_MEMORY = 256 * 1024     # 256KB SRAM
OFF_CHIP_BANDWIDTH = 32         # GB / s
CLOCK_SPEED = 1e9               # 1GHz
MICROSECOND = 1e6

# 1) Compute-unit (Systolic Array)
class SystolicArray:
    def __init__(self, PE_SIZE):
        self.PE_SIZE = PE_SIZE     # suppose 8 x 8 PE array
    
    def compute(self, A_tile, B_tile):
        
        start_time = time.time()

        result = np.dot(A_tile, B_tile)
        latency = (time.time() - start_time) * MICROSECOND   # convert to microsecond
        return result, latency

# 2) Memory-unit
class Memory:
    def __init__(self, SRAM_SIZE, bandwidth):
        self.SRAM_SIZE = SRAM_SIZE
        self.bandwidth = bandwidth          # OFF_CHIP_BANDWIDTH
    
    def load_tile(self, data_size):
        load_time = (data_size / self.bandwidth * CLOCK_SPEED)
        return load_time * MICROSECOND

# 3) Data Controller (Tiling)
class DataController:
    def __init__(self, TILE_SIZE):
        self.TILE_SIZE = TILE_SIZE
    
    def tile_matrices(self, A, B):
        A_tiles = [A[i:i+self.TILE_SIZE, j:j+self.TILE_SIZE]
                   for i in range(0, A.shape[0], self.TILE_SIZE)
                   for j in range(0, A.shape[1], self.TILE_SIZE)]
        B_tiles = [B[i:i+self.TILE_SIZE, j:j+self.TILE_SIZE]
                   for i in range(0, B.shape[0], self.TILE_SIZE)
                   for j in range(0, B.shape[1], self.TILE_SIZE)]
        return A_tiles, B_tiles


def simulate_NPU(A_shape, B_shape):
    compute_unit = SystolicArray(PE_SIZE)
    memory = Memory(ON_CHIP_MEMORY, OFF_CHIP_BANDWIDTH)
    controller = DataController(TILE_SIZE)

    
    # data
    if PRECISION == 16:
        A = np.random.rand(*A_shape).astype(np.float16)
        B = np.random.rand(*B_shape).astype(np.float16)
    else:
        A = np.random.rand(*A_shape).astype(np.int8)
        B = np.random.rand(*B_shape).astype(np.int8)

    A_tiles, B_tiles = controller.tile_matrices(A, B)

    compute_latency = 0
    memory_latency = 0

    for A_tile, B_tile in zip(A_tiles, B_tiles):
        _, compute_latency_per_tile = compute_unit.compute(A_tile, B_tile)
        compute_latency += compute_latency_per_tile
        
        latency_per_tile = memory.load_tile(A_tile.nbytes+B_tile.nbytes)
        memory_latency += latency_per_tile
    

    # FLOPs = 2 * output Size * filter
    flops = 2 * A_shape[0] * A_shape[1] * B_shape[1]
    throughput = flops/(compute_latency/MICROSECOND)
    peak_flops = PE_SIZE * PE_SIZE * CLOCK_SPEED * 2
    utilization = (throughput / peak_flops) * 100      # percentage

    
    print(f"-- RESULT {PRECISION}--")
    print(f" Total Compute Latency: {compute_latency:.2f} µs")
    print(f" Total Memory Latency: {memory_latency:.2f} µs")
    print(f" Throughput: {throughput / 1e9:.2f} GFLOPs/sec")
    print(f" Compute Utilization: {utilization:.2f} %")

simulate_NPU(A_shape=(64, 64), B_shape=(1024, 128))
