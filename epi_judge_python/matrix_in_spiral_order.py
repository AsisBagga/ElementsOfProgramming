def matrix_in_spiral_order(sm: list[list]) -> list:
    dir = 0
    top = 0
    down = len(sm) - 1
    left = 0
    right = len(sm) - 1
    op = []
    while (top<=down and left <=right):
        # this is for left to right
        if dir == 0:
            #print("left to right")
            for i in range(left, right+1):
                print(sm[top][i])
                op.append(sm[top][i])
            top = top + 1
        # this is for top to down
        elif dir == 1:
            #print("top to down")
            for i in range(top, down+1):
                print(sm[i][right])
                op.append(sm[i][right])
            right = right - 1
        # this is for left to right
        elif dir == 2:
            #print("right to left")
            for i in range(right, left-1, -1):
                print(sm[down][i])
                op.append(sm[down][i])
            down = down - 1
        # this is for down to top
        elif dir == 3:
            #print("down to top")
            for i in range(down, top-1, -1):
                print(sm[i][left])
                op.append(sm[i][left])
            left = left + 1
        dir = dir + 1
        dir = dir % 4
    return op

matrix_in_spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]])