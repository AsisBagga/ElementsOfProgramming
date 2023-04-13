def rotate_matrix(RM):
    def transpose_matrix(RM):
        for i in range(len(RM)):
            for j in range(i, len(RM)):
                RM[i][j], RM[j][i] = RM[j][i], RM[i][j]
                
        return RM
    def reverse_matrix(RM):
        for i in range(len(RM)//2):
            for j in range(len(RM)):
                RM[j][i], RM[j][len(RM)-1-i] = RM[j][len(RM)-1-i], RM[j][i]
        return RM
    RM = transpose_matrix(RM)
    return reverse_matrix(RM)
    
def print_matrix(RM, *args):
    for i in RM:
        print(i)
    if args:
        print(args[0])
print_matrix([[1,2,3],[4,5,6],[7,8,9]], "\n")
print_matrix(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))