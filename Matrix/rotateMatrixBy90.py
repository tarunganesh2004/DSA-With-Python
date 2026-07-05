# LC 48

def rotateImage(mat):
    n=len(mat)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(len(mat)):
        mat[i].reverse()


m= [[1,2,3],[4,5,6],[7,8,9]]

rotateImage(m)
for r in range(len(m)):
    print(m[r])