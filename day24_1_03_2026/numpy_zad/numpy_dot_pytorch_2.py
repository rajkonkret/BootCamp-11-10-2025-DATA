import torch
import time
import random
import numpy as np
from typing import Tuple

if torch.backends.mps.is_available():
    # device = torch.device("cpu")
    device = torch.device("mps")  # dla maca
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"Używane urządzenie: {device}")


def generate_random_tensor(shape: Tuple[int, int]) -> torch.Tensor:
    cpu_data = [
        [random.random() for _ in range(shape[1])]
        for _ in range(shape[0])
    ]
    return torch.tensor(cpu_data, dtype=torch.float32).to(device)


print("=" * 30)
print("Genrowanie tablic tensorów")
TORCH_ARRAY_A = generate_random_tensor((10000, 10000))
# TORCH_ARRAY_A = generate_random_tensor((5000, 5000))
TORCH_ARRAY_B = generate_random_tensor((10000, 10000))
# TORCH_ARRAY_B = generate_random_tensor((5000, 5000))

print("=" * 30)

if device.type == "cuda":
    torch.cuda.synchronize()

start_time = time.time()
gpu_result = torch.matmul(TORCH_ARRAY_A, TORCH_ARRAY_B)

if device.type == "cuda":
    torch.cuda.synchronize()

gpu_exec_time = time.time() - start_time
print(f"Czas wykonania na {device}: {gpu_exec_time:.6f} s")

CPU_ARRAY_A = TORCH_ARRAY_A.cpu().numpy()
CPU_ARRAY_B = TORCH_ARRAY_B.cpu().numpy()

print("=" * 30)
start_time = time.time()
numpy_result = np.dot(CPU_ARRAY_A, CPU_ARRAY_B)
numpy_exec_time = time.time() - start_time
print(f"Czas wykonania na numpy: {numpy_exec_time:.6f} s")

gpu_cpu = gpu_result.cpu()
numpy_tensor = torch.from_numpy(numpy_result)

abs_diff = torch.abs(gpu_cpu - numpy_tensor)
sum_diff = torch.sum(abs_diff)
max_diff = torch.max(abs_diff)

print(f"Suma różnic: {sum_diff.item():.10f}")
print(f"Maksymalna różnica: {max_diff.item():.10f}")
print(f"Zgodność wyników: {torch.allclose(gpu_cpu, numpy_tensor, atol=1e-4, rtol=1e-4)}")
# Używane urządzenie: mps
# ==============================
# Genrowanie tablic tensorów
# ==============================
# Czas wykonania na mps: 0.056313 s
# ==============================
# Czas wykonania na numpy: 1.919109 s
# Suma różnic: 502.0700683594
# Maksymalna różnica: 0.0178222656
# Zgodność wyników: True
# mlx
