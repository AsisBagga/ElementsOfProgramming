'''
    D = [1,2,9]
    so it becomes 129
    add one to it = 130
    return [1,3,0]
'''
def plus_one(A):
    if A[len(A)-1] == 9:
        A[len(A) - 1] = 0
        i = len(A) - 2
        while True:
            if A[i] != 9:
                A[i] += 1
                break
            else:
                A[i] = 0
            #Case in which array is multiple of 9s
            if i == 0:
                A[0] = 1
                A.append(0)
                return A
            i -= 1
        return A
    A[len(A)-1] += 1
    return A
print(plus_one([1,2,9]))
print(plus_one([1,2,9]))
print(plus_one([1,9,9]))
print(plus_one([9,9,9]))
print(plus_one([10,9,9]))