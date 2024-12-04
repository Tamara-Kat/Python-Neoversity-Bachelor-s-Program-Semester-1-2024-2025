from typing import List


def check(
    row_start: int, row_end: int, column_start: int, column_end: int
) -> List[List[int]]:
    result = []
    for i in range(row_start, row_end + 1):
        tmp = []
        for j in range(column_start, column_end + 1):
            tmp.append(i * j)
        result.append(tmp)
    return result

    # return [
    #     [i * j for j in range(column_start, column_end + 1)]
    #     for i in range(row_start, row_end + 1)
    # ]


print(check(2, 4, 3, 7))
