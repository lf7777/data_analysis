#阶 乘 :
#能够计算在一个样本里,取不同的次数,能得到多少种结果.
#Cn^m = m!/n!*(m-n)!

def fac(m,n):
    f1 = 1
    for x in range(m,0,-1):
        f1 *= x

    f2 = 1
    for x in range(n,0,-1):
        f2 *= x

    f3 = 1
    for x in range((m-n),0,-1):
        f3 *= x 

    return f1/(f2*f3)

print(int(fac(5,2)))
