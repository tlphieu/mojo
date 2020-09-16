#so hoan hao
def sohoanhao(n):
    s = 0
    for i in range(1,n):
        if n%i ==0:
            s = s + i
    if(n == s):
        print("so hoan hao :", n)
    else:
        print("khong la so hoan hao:")
    return s
a= int(input("nhap so n:"))
sohoanhao(a)
