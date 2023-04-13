from typing import List

from test_framework import generic_test
from collections import defaultdict

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(S: List[List[int]]) -> bool:
    row = defaultdict(set)
    coll = defaultdict(set)
    square = defaultdict(set)
    for r in range(len(S)):
        for c in range(len(S)):
            if S[r][c] == 0:
                continue
            if S[r][c] in row[r] or S[r][c] in coll[c] or S[r][c] in square[(r//3, c//3)]:
                return False
            row[r].add(S[r][c])
            coll[c].add(S[r][c])
            square[(r//3, c//3)].add(S[r][c])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
