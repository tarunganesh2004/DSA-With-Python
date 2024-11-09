from calendar import c


p=[60,100,120]
w=[10,20,30]
cap=50

def fractional(p,w,cap):
        pw=[]
        for i in range(len(p)):
            pw.append((p[i],w[i])) 

        # sort based on p/w ratios
        pw.sort(key=lambda x: x[0]/x[1], reverse=True)

        maxProfit=0.0
        remaining=cap

        for price,wei in pw:
            if wei<=remaining:
                maxProfit+=price
                remaining-=wei
            else:
                maxProfit+=price*(remaining/wei)
                break
        return maxProfit

print(fractional(p,w,cap))