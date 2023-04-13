def delete_duplicates(A):
    w = 1
    for i in range(1, len(A)):
        if A[w-1] != A[i]:
            A[w]=A[i]
            w += 1
    print(A)
    return w
print(delete_duplicates([2,3,5,5,7,11,11,13]))