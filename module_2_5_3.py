def get_matrix(n,m,value):
    if n<=0 or m<=0:
        return []
    matrix=[]
    for i in range(n):
        row = []
        for k in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
print(get_matrix(2,2,10))
print(get_matrix(3,4,42))
print(get_matrix(4,2,13))