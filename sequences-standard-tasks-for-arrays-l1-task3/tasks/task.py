from typing import Dict
from collections import Counter

def get_dict(s: str) -> Dict[str, int]:
    # Приводимо рядок до нижнього регістру
    s = s.lower()
    # Підраховуємо частоту кожного символу
    frequency = Counter(s)
    return dict(frequency)
