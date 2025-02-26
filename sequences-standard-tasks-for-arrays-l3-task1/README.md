# Simple Validator for a Sudoku Board

Suppose you are tasked with designing a simple validator for a partially filled 9x9 Sudoku board. Your primary job is to check if the current entries on the board follow the Sudoku rules or not. Your task is to return a Boolean that states whether the board is valid or not.

## Validation Rules

The rules for an entry to be valid are as follows:

1. **Row Validation**: Each row of the board can contain digits 1–9 without any repetitions.
2. **Column Validation**: Each column of the board can contain digits 1–9 without any repetitions.
3. **Sub-box Validation**: Each of the nine 3x3 sub-boxes of the grid must contain the digits 1–9 without repetitions.

   **Note**: Each 3x3 sub-box contains nine cells, there are nine sub-boxes, and each cell belongs to only one sub-box. There is only one way to place them. If you are still not sure you understand, read the Sudoku rules.

## Important Considerations

It's important to keep in mind that:

- The Sudoku board can be partially filled, and it can be valid but not necessarily solvable.
- 42.	You are only expected to verify the existing filled entries. Unfilled entries are not part of the validation process

## Task

Your function will receive a 9x9 2D array (matrix) as input, representing the Sudoku board. The empty cells will be represented by the `.` character. Return `True` if the board is valid according to the Sudoku rules and `False` otherwise.

## Example

```python
>>> validate_sudoku([
        ['3', '.', '6', '5', '.', '8', '4', '.', '.'], 
        ['5', '2', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '8', '7', '.', '.', '.', '.', '3', '1'], 
        ['.', '.', '3', '.', '1', '.', '.', '8', '.'], 
        ['9', '.', '.', '8', '6', '3', '.', '.', '5'], 
        ['.', '5', '.', '.', '9', '.', '6', '.', '.'], 
        ['1', '3', '.', '.', '.', '.', '2', '5', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '7', '4'], 
        ['.', '.', '5', '2', '.', '6', '3', '.', '.'] 
    ])
True
```

___*Please keep in mind the following___:
 
- _Do not use the "input" function to enter initial parameters for your task solution._  
- _Do not use the "print" function to return results from your task solution. Do not delete code from the template or change predefined - functions._
- _Put your solution in the section marked with the comment "Put your code here." You can still use your own functions and define them outside the predefined function._
