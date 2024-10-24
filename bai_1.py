import math
r=float(input("nhap ban kinh: ")) 
h=float(input("nhap chieu cao: "))
pi = 3.14
dtxq = 2*pi*r*h
dttp = dtxq + 2*pi*r**2
the_tich = pi*r**2*h
if r > 0 and h > 0:
   print(f"Dien tich xung quanh: {dtxq:.2f}")
   print(f"Dien tich toan phan: {dttp:.2f}")
   print(f"The tich: {the_tich:.2f}")
else:
   print("Loi gia tri vui long nhap lai") 
print("ket thuc chuong trinh")   