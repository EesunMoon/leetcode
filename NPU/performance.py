"""
    Now you know that XNet has a fully connected layer with input dimension 1024
    and output dimension 1024 * 256 at the end of network.
    Design a simulator npuSim() which predicts the expected latency for computation,
    expected on-chip memory capacity, and expected latency for data fetching.

    You can add any variable that you need.
"""

operation = ("linear", (1024, 1024*256))

class npuSim():
    def __init__(self):
        self.clock = 500 * (10**6)  # 500MHz
        self.numPE = 256
        self.dramBW = 64            # 64 GB/s

        # operation = ("linear", (1024, 1024*256))
        self.optype = operation[0]
        self.opsize = operation[1]

        self.precision = 16         # FP16 (bits per element)
    
    def compute(self):
        """ expected latency for computation """
        
        # compute-latency = FLOPs / clock * numPE
        if self.optype == "linear":
            B = self.opsize[0]
            M, N = self.opsize[0], self.opsize[1]//self.opsize[0]
            FLOPs = 2 * B * M * N
            output_size = B * N
        elif self.optype == "gemm":
            # ex) (256*1024, 1024*128) => output (256 * 128)
            N, M = self.opsize[0]
            M, K = self.opsize[1]
            output_size = N * K
            FLOPs = 2 * output_size * M
        elif self.optype == "conv":
            F, _, K, C = self.opsize[1] # filter size
            N, _, C = self.opsize[2]    # output size (N = (input size - filter size + 2 padding)/stride+1) 
            filter_size = F * F * K
            output_size = N * N * C
            FLOPs = 2 * filter_size * output_size
        elif self.optype == "element":
            B, M = self.opsize[0], self.opsize[1]
            FLOPs = B * M
        latency = FLOPs / (self.clock * self.numPE)
        return latency

    def memory(self):
        """ expected on-chip memory capacity (SRAM usage) """
        a_load = self.opsize[0] * (self.precision // 8)     # convert to bytes
        b_load = self.opsize[1] * (self.precision // 8)     # convert to bytes
        output_size = self.opsize[1] // self.opsize[0]      # in the case of linear
        out_load = output_size * (self.precision // 8)      # convert to bytes
        
        capacity = a_load+b_load+out_load
        return capacity

    def bandwidth(self):
        """ expected latency for data fetching """
        # (a_load, b_load, output_load) / DRAM_BW
        capacity = self.memory()
        bandwidth = capacity / self.dramBW
        return bandwidth
