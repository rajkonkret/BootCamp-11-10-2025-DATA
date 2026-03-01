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
