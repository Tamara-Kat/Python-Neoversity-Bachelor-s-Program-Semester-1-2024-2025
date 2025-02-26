from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    return tuple(int(digit) for digit in str(num))
