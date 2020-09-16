n = int(input("nhap so tu nhien:"))
u = int;
mindigit = 9
maxdigit =0
if n < 10 :
    maxdigit = mindigit = n
else :
    while n > 0 :
        u = n%10
        maxdigit = max(maxdigit,u)
        mindigit = min(mindigit,u)
        n=n//10
print("chu so nho nhat:", mindigit)
print("chu so lon nhat: ", maxdigit)