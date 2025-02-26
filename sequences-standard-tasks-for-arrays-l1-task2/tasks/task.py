from typing import List, Tuple

def get_pairs(lst: List) -> List[Tuple]:
    if len(lst) < 2:
        return []
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]


