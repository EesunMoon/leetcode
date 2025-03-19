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

"""
    analyze performance

    [Compute-bound (computation tiling) :: SRAM <-> PE]
        theorical compute latency (sec) = total FLOPs / (Clock Speed * numPE)
            total FLOPs = output size * 2
        compute utilization (percentage) = actual compute latency / theorical compute latency * 100
    [Memory-bound (memory tiling) DRAM <-> SRAM]
        theorical memory transfer time (sec) = total data transfer / Dram BW
        Memory BW (GB/s) = total data transfer / actual memory transfer time
        memory utilization (percentage) = Memory BW / Dram BW * 100

"""


class NPU_simulation:
    def __init__(self, input_size, weight_size, output_size, PRECISION, optype):
        self.A_size = input_size
        self.B_size = weight_size
        self.output_size = output_size
        self.optype = optype
        self.PRECISION = PRECISION           # INT8, FP16
        
        # 0) Define parameter
        self.numPE = 64                      # Number of systolic array cores: 8 x 8
        # self.numPE = 16                    # self.numPE = 256 (16 x 16)
        self.sram_memory = 256 * 1024       # 256KB SRAM
        self.dramBW = 64                     # GB / s
        self.CLOCK_SPEED = 500 * (10**6)     # 500MHz

        self.TILE_SIZE = 8                   # convolution -> systolic, output stationary

    
        self.compute_latency = 0
        self.memory_latency = 3.5           # suppose
        self.res_data = 0


    def tile_matrices(self, A, B):
        """ Data Controller (Tiling) """

        A_tiles = [A[i:i+self.TILE_SIZE, j:j+self.TILE_SIZE]
                   for i in range(0, A.shape[0], self.TILE_SIZE)
                   for j in range(0, A.shape[1], self.TILE_SIZE)]
        B_tiles = [B[:,:,:,k] for k in range(B.shape[3])]
        return A_tiles, B_tiles
    
    def VectorStyle(self, A_tile, B_tile):
        """ compute-unit: (1) Vector Style """
        start_time = time.time()

        result = np.dot(A_tile, B_tile)
        latency = (time.time() - start_time)
        return result, latency              # convert to microsecond
    
    def SystolicArray(self, A_tile, B_tile):
        """ compute-unit: (2) systolic array """
        start_time = time.time()
        
        output_channels = B_tile.shape[1]
        result = np.zeros((self.TILE_SIZE, output_channels))
        
        for step in range(2*self.TILE_SIZE-1):
            for i in range(self.TILE_SIZE):
                for j in range(output_channels):
                    k = step-i
                    if 0 <= k < A_tile.shape[1]:
                        result[i, j] += A_tile[i, k] * B_tile[k,j]
        latency = (time.time() - start_time)
        return result, latency


    def simulate(self):
        # make data
        if self.PRECISION == 16:
            A = np.random.rand(*self.A_size).astype(np.float)
            B = np.random.rand(*self.B_size).astype(np.float)
            self.output = np.zeros(self.output_size).astype(np.float)
        else:
            A = np.random.rand(*self.A_size).astype(np.int8)
            B = np.random.rand(*self.B_size).astype(np.int8)
            self.output = np.zeros(self.output_size).astype(np.int8)


        # tiling
        A_tiles, B_tiles = self.tile_matrices(A, B)

        for A_tile, B_tile in zip(A_tiles, B_tiles):
            if self.optype == "linear":
                flops = 2 * self.output[0] * self.output[1]
                res_tile, compute_latency_per_tile = self.VectorStyle(A_tile, B_tile)
            elif self.optype == "conv":
                flops = 2 * self.B_size[0] * self.B_size[1] * self.B_size[2] * self.output_size[0] * self.output_size[1] * self.output_size[2]
                res_tile, compute_latency_per_tile = self.SystolicArray(A_tile, B_tile)
            elif self.optype == "gemm":
                flops = 2 * self.output_size[0] * self.output_size[1] * self.output_size[2]
                res_tile, compute_latency_per_tile = self.SystolicArray(A_tile, B_tile)
            elif self.optype == "element":
                flops = 0
                res_tile, compute_latency_per_tile = self.VectorStyle(A_tile, B_tile)
            self.compute_latency += compute_latency_per_tile

            self.res_data += res_tile.nbytes

        # performance analysis
        """
            [Compute-bound (computation tiling) :: SRAM <-> PE]
                theorical compute latency (sec) = total FLOPs / (Clock Speed * numPE)
                    total FLOPs = output size * 2
                compute utilization (percentage) = actual compute latency / theorical compute latency * 100
            [Memory-bound (memory tiling) DRAM <-> SRAM]
                theorical memory transfer time (sec) = total data transfer / Dram BW
                Memory BW (GB/s) = total data transfer / actual memory transfer time
                memory utilization (percentage) = Memory BW / Dram BW * 100"
        """

        # compute
        theorical_compute_latency = flops / (self.CLOCK_SPEED * self.numPE)
        throughput = flops / self.compute_latency
        compute_utilization = self.compute_latency / theorical_compute_latency * 100

        # memory
        total_memory = A.nbytes + B.nbytes + self.res_data # read, write
        memory_BW = total_memory / self.memory_latency
        memory_utilization = memory_BW / self.dramBW * 100
        
    
        return self.compute_latency, compute_utilization, throughput, self.memory_latency, memory_utilization


if __name__ == "__main__":
    # convolution: 224 x 224 x 3 -> last layer's output 7 x 7 x 1024
    # transformer: 212 
    # input 112*112*64
    # weight 3*3*64*128
    # output (~112)*(~112)*128

    input_size = (112, 112, 64)
    weight_size = (3, 3, 64, 128)
    output_size = (112, 112, 128)


    for precision in [8, 16]:
        NPU = NPU_simulation(input_size, weight_size, output_size, precision, "conv")
        compute_latency, compute_utilization, throughput, memory_latency, memory_utilization = NPU.simulate()

        print(f"-- RESULT {precision}--")
        print(f" [Compute] Latency: {compute_latency:.2f} s")
        print(f" [Compute] Utilization: {compute_utilization:.2f} %")
        print(f" [Compute] Throughput: {throughput:.2f} %")
        print(f" [Memory] Latency: {memory_latency:.2f} s")
        print(f" [Memory] Utilization: {memory_utilization:.2f} %")
