n = int (input("nhap so n: "))
s = 0
while n > 0:
  dv = n%10
  n = n // 10
  s = s + dv
print("tong cac chu so : ", s, "\n")