
# start with cuda
#  MH, October 2026

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


#%%
# GPU
cuda_available = torch.cuda.is_available()
print(f"\nCUDA Available     : {cuda_available}")
if cuda_available:
    device_count = torch.cuda.device_count()
    device_name = torch.cuda.get_device_name(0)
    print(f"GPU Name           : {device_name}")

    cuda_ver = torch.version.cuda
    device_name = torch.cuda.get_device_name(0)
    cap_major, cap_minor = torch.cuda.get_device_capability(0)
    
    print(f"CUDA Version       : {cuda_ver}")
    print(f"Compute Capability : sm_{cap_major}{cap_minor}")


#%%
# B) CPU 

def run_matmul(a, b, num_threads=1):

    start = time.perf_counter()
    torch.set_num_threads(num_threads)
    _ = torch.matmul(a, b)
    end = time.perf_counter()

    time_taken = end - start
    gflops = (2 * N**3) / (time_taken * 1e9)  # Calculate GFLOPS
    # print(f"threads: {num_threads}, time: {time_taken:.2f} s, GFLOPS: {gflops:.1f}")
    print(f"threads: {num_threads:>2d}, time: {time_taken:>6.2f} s, GFLOPS: {gflops:>6.1f}")

    return

#  loop over n threads 1,2,4,8 ...
N = 8000
PRECISION = torch.float32
a_cpu = torch.randn(N, N, dtype=PRECISION)
b_cpu = torch.randn(N, N, dtype=PRECISION)

num_threads = 1
while num_threads <= n_threads:
    run_matmul(a_cpu, b_cpu, num_threads=num_threads)
    num_threads = num_threads + 1


#%%
# C) GPU

N = 10000
PRECISION = torch.float32
a_cpu = torch.randn(N, N, dtype=PRECISION)
b_cpu = torch.randn(N, N, dtype=PRECISION)


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

gflops = (2 * N**3) / (gpu_time * 1e9)  # Calculate GFLOPS
print(f"GPU:    {gpu_time:.4f} seconds, GFLOPS: {gflops:.1f}\n")


# %%
