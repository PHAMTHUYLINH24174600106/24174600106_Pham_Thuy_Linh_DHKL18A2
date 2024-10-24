import math

x = float(input("nhap gia tri: ")) 
if x > 0 and x != 1 :
    print("gia tri thoa man")
else :
     print(" Loi gia tri ") 
logx4 = math.log(x,4)
log2x = math.log(2,x)
f_x = logx4 + log2x
print(f"Gia tri can tim x:{f_x:.2f}")    