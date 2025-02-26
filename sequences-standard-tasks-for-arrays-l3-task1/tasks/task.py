def validate_sudoku(board: list[list[str]]) -> bool:
    def is_valid_block(block: list[str]) -> bool:
        block = [num for num in block if num != '.']
        return len(block) == len(set(block))

    # Перевірка рядків
    for row in board:
        if not is_valid_block(row):
            return False

    # Перевірка стовпців
    for col in range(9):
        if not is_valid_block([board[row][col] for row in range(9)]):
            return False

    # Перевірка підблоків 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_block(
                    [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            ):
                return False

    return True


# Приклад використання
board = [
    ['3', '.', '6', '5', '.', '8', '4', '.', '.'],
    ['5', '2', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '8', '7', '.', '.', '.', '.', '3', '1'],
    ['.', '.', '3', '.', '1', '.', '.', '8', '.'],
    ['9', '.', '.', '8', '6', '3', '.', '.', '5'],
    ['.', '5', '.', '.', '9', '.', '6', '.', '.'],
    ['1', '3', '.', '.', '.', '.', '2', '5', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '7', '4'],
    ['.', '.', '5', '2', '.', '6', '3', '.', '.']
]

print(validate_sudoku(board))  # Виведе: True

