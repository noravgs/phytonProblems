# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

from typing import List  # Import List for type hinting

def isValidSudoku(board: List[List[str]]) -> bool:
    # Initialize lists of sets to track seen numbers in rows, columns, and boxes
    rows = [set() for _ in range(9)]  # Create a list of 9 sets for each row
    columns = [set() for _ in range(9)]  # Create a list of 9 sets for each column
    boxes = [set() for _ in range(9)]  # Create a list of 9 sets for each 3x3 box

    # Iterate through each cell in the 9x9 board
    for i in range(9):  # Loop through each row index
        for j in range(9):  # Loop through each column index
            num = board[i][j]  # Get the value in the current cell
            if num != ".":  # Check if the cell is not empty
                # Check the row for duplicates
                if num in rows[i]:  # If the number is already in the row set
                    return False  # Return False since it's an invalid Sudoku
                rows[i].add(num)  # Add the number to the corresponding row set

                # Check the column for duplicates
                if num in columns[j]:  # If the number is already in the column set
                    return False  # Return False since it's an invalid Sudoku
                columns[j].add(num)  # Add the number to the corresponding column set

                # Check the 3x3 box for duplicates
                box_index = (i // 3) * 3 + (j // 3)  # Calculate the index of the 3x3 box
                if num in boxes[box_index]:  # If the number is already in the box set
                    return False  # Return False since it's an invalid Sudoku
                boxes[box_index].add(num)  # Add the number to the corresponding box set

    return True  # If no duplicates were found, return True (valid Sudoku)
