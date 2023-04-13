import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:

    '''This one is when a user wants to give an array of
    boolean values and expect all false values at start of the array'''

    smaller, equal = 0, 0
    larger = len(A)

    while equal < larger:
        if A[equal] == False:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
    print(A)

    '''Another Implementation with while loop much easier to understand'''
    # p = A[pivot_index]
    # smaller = 0
    # equal = 0
    # larger = len(A)
    # while equal < larger:
    #     if A[equal] < p:
    #         A[smaller], A[equal] = A[equal], A[smaller]
    #         smaller += 1
    #         equal += 1
    #     elif A[equal] == p:
    #         equal += 1
    #     else:
    #         larger -= 1
    #         A[larger], A[equal] = A[equal], A[larger]

    print(A)
    '''This is for O(n) Time complexity'''
    # pivot_val = A[pivot_index]
    # # first pass for smaller array than pivot
    # smaller = 0
    # for i in range(len(A)):
    #     print(A, i , smaller)
    #     if A[i] < pivot_val:
    #         A[smaller], A[i] = A[i], A[smaller]
    #         smaller += 1
    # print("After first Pass ", A)
    # larger = len(A) -1
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot_val:
    #         A[larger], A[i] = A[i], A[larger]
    #         larger -= 1
    #print("After 2nd Pass ", A)
    '''This is for O(n^2) Time Complexity'''
    # pivot_val = A[pivot_index]
    # for i in range(len(A)):
    #     # putting all the items gratter than pivot to left
    #     for j in range(i+1, len(A)):
    #         print("Before Swap:", A, " i ", i, " j ", j)
    #         if A[j] < pivot_val:
    #             A[i],A[j] = A[j], A[i]
    #             print("After swap",  A, " i ", i, " j ", j)
    #             break
    # print("++")
    # for i in reversed(range(len(A))):
    #     # putting all the items gratter than pivot to right
    #     for j in reversed(range(i)):
    #         print("Before Swap:", A, " i ", i, " j ", j)
    #         if A[j] > pivot_val:
    #             A[i],A[j] = A[j], A[i]
    #             print("After swap",  A, " i ", i, " j ", j)
    #             break
    return
@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')

if __name__ == '__main__':
    #A = [0,1,1,64,32,7,1,4]
    A = [True, False, False, True, True, False, True]
    dutch_flag_partition(0, A)
    #exit(
    #   generic_test.generic_test_main('dutch_national_flag.py',
    #                                  'dutch_national_flag.tsv',
    #                                  dutch_flag_partition_wrapper))
