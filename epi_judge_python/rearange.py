def rearange(A:list) -> list:
    A = sorted(A)
    for i in range(1, len(A)-1):
        if i %2 != 0:
            A[i], A[i+1] = A[i+1], A[i]
    return A

print(rearange([1,2,3,4,5,6,7,8,9,10,11]))