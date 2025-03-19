"""
Convolution
    Activation size = M * M * L
    Weight size = F * F * L * K
    Output size = N * N * K

    activation[0:M][0:M][0:L]
    weight[0:F][0:F][0:L][0:K]
    output[0:N][0:N][0:K]

    N = (M-F+2P)/S + 1

--
    Convolution:: compute-bound
        tiling << memory loader
            Tr: output x direction tiling size
            Tc: output y direction tiling size
            Tk: output channel direction tiling size
            SRAM = S
                => output tiling iteration = (N*N*K)/S

        systolic << compute parallelism
            Vector = V
    
"""

# FLOPs = N * N * K * L * F * F * 2 << compute-bound
for ch_o in range(K):         # Output Channel (K)
    for ox in range(N):       # Output X dimension
        for oy in range(N):   # Output Y dimension
            
            psum = 0
            for ch_in in range(L):  # Input Channel (L)
                for fx in range(F):  # Filter X dimension
                    for fy in range(F):  # Filter Y dimension
                        psum += activation[ox+fx][oy+fy][ch_in] * weight[fx][fy][ch_in][ch_o]
                
            output[ox][oy][ch_o] = max(0, psum)  # Activation: ReLU


## Optimization
# => Tiling + Vectorization


# -- Off-chip memory (DRAM)
for ch_o in range(0, K, Tk):        # output channel (K)
    for ox in range(0, N, Tr):      # output X dim
        for oy in range(0, N, Tc):  # output Y dim

            # -- On-chip memory (SRAM)
            for tk in range(Tk):
                for tr in range(Tr):
                    for tc in range(Tc):

                        # -- Register ( Vector: V ): Parallelism
                        for v in range(V):
                            psum = 0                        # accumulation (f * f * ch_in) - output stationary
                            for ch_in in range(0, L, tile_size):       # input channel (L)
                                for fx in range(F):      # filter X dim
                                    for fy in range(F):  # filter y dim
                                        psum += (activation[ox+fx][oy+fy][ch_in+v] * 
                                                 weight[fx][fy][ch_in+v][ch_o+tk])
                                
                            output[ox+tr][oy+tc][ch_o+tk] = max(0, psum) # activation function - ReLU
