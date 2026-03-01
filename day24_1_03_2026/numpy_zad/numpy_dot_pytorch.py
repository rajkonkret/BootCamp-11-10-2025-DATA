import torch
import time
import random
import numpy as np
from typing import Tuple

# wybór urzadzenia: GPU jeśli dostepne, inaczej CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Używane urządzenie: {device}")


def generate_random_tensor(shape: Tuple[int, int]) -> torch.Tensor:
    cpu_data = [
        [random.random() for _ in range(shape[1])]
        for _ in range(shape[0])
    ]

    return torch.tensor(cpu_data, dtype=torch.float32).to(device)


TORCH_ARRAY_A = generate_random_tensor((500, 500))
TORCH_ARRAY_B = generate_random_tensor((500, 500))

# mnożenie macierzy
print("=" * 30)
start_time = time.time()
gpu_result = torch.matmul(TORCH_ARRAY_A, TORCH_ARRAY_B)
gpu_exec_time = time.time() - start_time
print(f"Czas wykonania na: {device}: {gpu_exec_time:.6f} s")

# konwerja na numpy
CPU_ARRAY_A = TORCH_ARRAY_A.cpu().numpy()
CPU_ARRAY_B = TORCH_ARRAY_B.cpu().numpy()

print("=" * 30)
start_time = time.time()
numpy_result = np.dot(CPU_ARRAY_A, CPU_ARRAY_B)
numpy_exec_time = time.time() - start_time
print(f"Czas wykonania na: numpy: {numpy_exec_time:.6f} s")

# Porównanie wyników
diff = torch.sum(torch.abs(gpu_result.cpu() - torch.tensor(numpy_result)))
print(f"Różnica między GPU a CPU: {diff.item():.10f}")
print(f"Zgodność wyników: {diff.item() < 1e-5}")

# https://colab.research.google.com/drive/1x1aco1LDTlkMnu9nCw4nmBPL8G9U2I8L#scrollTo=aOiQbjI1_OzX
