#%%
# start with cuda


#%%
#  A) libs and start, system info
import pandas as pd
import numpy as np
import torch
import time
import socket
import platform
import psutil
import os

print("System Information:")
print("computer        :", socket.gethostname())
print("OS              :", platform.system())
if (platform.system()=='Windows'):
    print("user            :", os.getenv("USERNAME"))
else:
    print("user            :", os.getenv("USER"))

print("path            :", os.getcwd())


#  CPU
n_cores = psutil.cpu_count(logical=False)
n_threads = os.cpu_count() 
print("CPU cores       :", n_cores)
print("CPU threads     :", n_threads)


# GPU
cuda_available = torch.cuda.is_available()
print(f"CUDA Available  : {cuda_available}")
if cuda_available:
    device_count = torch.cuda.device_count()
    device_name = torch.cuda.get_device_name(0)
    print(f"GPU Name        : {device_name}")



#%%
# B) single-core CPU 


# Define matrix size (4000 x 4000 float32 elements)
N = 4000
print(f"Benchmarking {N}x{N} Matrix Multiplication...\n")

# 1. CPU Single-Core Benchmark
torch.set_num_threads(1)
a_cpu = torch.randn(N, N)
b_cpu = torch.randn(N, N)

start = time.perf_counter()
_ = torch.matmul(a_cpu, b_cpu)
cpu_1thread_time = time.perf_counter() - start
print(f"CPU (1 Thread):   {cpu_1thread_time:.4f} seconds")


# 2. CPU Multi-Core Benchmark (All 16 threads on Ryzen 5700X)
torch.set_num_threads(8)
start = time.perf_counter()
_ = torch.matmul(a_cpu, b_cpu)
cpu_multithread_time = time.perf_counter() - start
print(f"CPU (16 Threads):  {cpu_multithread_time:.4f} seconds")


flops = (2 * N**3) / 1e9  # 128 GFLOPs

print(f"1 Thread  :  {flops / cpu_1thread_time:.2f} GFLOPS")
print(f"16 Threads: {flops / cpu_multithread_time:.2f} GFLOPS")




#%%


# 3. GPU Benchmark (GTX 1060)
a_gpu = a_cpu.to("cuda")
b_gpu = b_cpu.to("cuda")

# Warm-up run to initialize CUDA context
_ = torch.matmul(a_gpu, b_gpu)
torch.cuda.synchronize()

# Timed GPU run
start = time.perf_counter()
_ = torch.matmul(a_gpu, b_gpu)
torch.cuda.synchronize()  # Force CPU to wait until GPU finishes computation
gpu_time = time.perf_counter() - start

print(f"GPU (GTX 1060):    {gpu_time:.4f} seconds\n")

# Speedup comparison
print(f"--> GPU Speedup vs 1 Thread:  {cpu_1thread_time / gpu_time:.2f}x faster")
print(f"--> GPU Speedup vs 16 Threads: {cpu_multithread_time / gpu_time:.2f}x faster")