import os

k_vals = [1, 2, 5, 10, 20, 50, 100]

for k in k_vals:
    print(f"Running for k: {k}")
    os.system(f"python run.py --algorithm milvus-hnsw --dataset glove-100-angular --count {k}")
    print(f"Finished for k: {k}")
