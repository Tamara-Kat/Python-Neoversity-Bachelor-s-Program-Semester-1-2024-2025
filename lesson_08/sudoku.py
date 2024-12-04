def validate_sudoku(board: list[list[str]]) -> bool:
    # Helper function to check if a list contains duplicates
    def has_duplicates(nums: list[str]) -> bool:
        # Filter out '.' and create a set of numbers
        seen = set()
        for num in nums:
            if num != ".":
                if num in seen:
                    return True
                seen.add(num)
        return False

    # 1. Check rows
    for row in board:
        if has_duplicates(row):
            return False

    # 2. Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if has_duplicates(column):
            return False

    # 3. Check 3x3 sub-boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            # Get all numbers in current 3x3 box
            box_nums = []
            for i in range(3):
                for j in range(3):
                    box_nums.append(board[box_row + i][box_col + j])
            if has_duplicates(box_nums):
                return False

    return True
