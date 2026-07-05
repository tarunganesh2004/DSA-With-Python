def convert(k):
    n=len(k)
    r=k[:3]
    r.reverse()
    r1=k[3:]
    return r+r1
def rotate(mat):
    r=[]
    res=[]
    for i in range(len(mat)):
        l=[]
        for j in range(len(mat)):
            l.append(mat[j][i])
        r.append(l)
    
    for k in r:
        l=convert(k)
        res.append(l)

    for i in range(len(res)):
        print(res[i])
        
m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(m)
