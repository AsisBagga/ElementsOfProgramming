def can_reach_end(A, x):
    #Step1: start from A[1]
    #Step2: check the value of A[1] if its value is n then advance i + n steps
    #Step3: redo step2
    #Step4: if n == 0 then move out of the loop and check the value of i
    # if i is < len(0) return False else True
    i = x
    steps=0
    while i < len(A)-1:
        if not A[i]:
            break
        #i keep track of array position
        i = i + A[i]
        steps += 1
    if i < len(A):
        return False, None
    return True, steps
print(can_reach_end([3,3,1,0,2,0,1],1))
print(can_reach_end([3,2,0,0,2,0,1],1))
print(can_reach_end([0,0,0,0],1))
print(can_reach_end([9,9,9,9,9],1))
print(can_reach_end([2,4,1,1,0,2,3],1))
