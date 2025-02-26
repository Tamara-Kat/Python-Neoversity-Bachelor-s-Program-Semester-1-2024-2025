from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_vals = set()
    for d in lst:
        for value in d.values():
            unique_vals.add(value)
    return unique_vals


