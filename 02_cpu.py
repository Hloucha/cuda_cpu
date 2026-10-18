# start with CPU compute and copilot
# MH, October 2026

#%%
#  A) libs and start, system info
import pandas as pd
import numpy as np
import time
import socket
import platform
import psutil
import os
import multiprocessing


def sum_squared_distances_chunk(args):
    points, start, stop = args
    partial_sum = 0.0
    for j in range(start, stop):
        differences = points[j + 1:] - points[j]
        partial_sum += np.sum(differences * differences)
    return partial_sum


if __name__ == "__main__":
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
    # B) CPU 

    n  = 2000
    X = np.random.rand(n,3)

    time_start = time.time()

    # Original nested-loop calculation for comparison
    dist2_sum = 0
    for j in range(n):
        for k in range(j + 1, n):
            dist2_sum += (
                (X[j, 0] - X[k, 0]) ** 2
                + (X[j, 1] - X[k, 1]) ** 2
                + (X[j, 2] - X[k, 2]) ** 2
            )

    time_end = time.time()
    print("Nested-loop distance squared sum :", round(dist2_sum, 4))
    print("Nested-loop CPU time             :", round(time_end - time_start, 4), "seconds")


    #%%
    ##C)

    time_start = time.time()
    #  calculate total distance of particles
    #  Vectorized single-threaded NumPy version: faster than nested Python loops

    X2 = np.sum(X * X, axis=1)  # squared distance of each point from the origin


    dist2 = X2[:, None] + X2[None, :] - 2.0 * (X @ X.T) # distance between all pairs

    np.fill_diagonal(dist2, 0.0) # to avoid numerical issues

    dist2 = np.maximum(dist2, 0.0) 

    dist2_sum = dist2[np.triu_indices(n, k=1)].sum()


    time_end = time.time()

    print("Total distance squared sum :", round(dist2_sum, 4))
    print("CPU time                   :", round(time_end - time_start, 4), "seconds")



    #%%
    # D) Multiprocessing CPU calculation

    for label, requested_workers in (
        ("physical cores", n_cores),
        ("logical threads", n_threads),
    ):
        worker_count = max(1, min(requested_workers or 1, n - 1))
        chunk_size = max(1, (n - 1 + worker_count - 1) // worker_count)
        chunks = [
            (X, start, min(start + chunk_size, n - 1))
            for start in range(0, n - 1, chunk_size)
        ]
        
        time_start = time.time()
        with multiprocessing.Pool(processes=worker_count) as pool:
            partial_sums = pool.map(sum_squared_distances_chunk, chunks)
        dist2_sum_parallel = sum(partial_sums)
        time_end = time.time()
        
        print(f"Multiprocessing ({label}, {worker_count} workers) distance squared sum :",
              round(dist2_sum_parallel, 4))
        print(f"Multiprocessing ({label}) CPU time :", round(time_end - time_start, 4), "seconds")



# %%
