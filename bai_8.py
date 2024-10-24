import math
x = float(input("nhap gia tri: ")) 
if x > 0 and x != 1 :
    logx4 = math.log(x,4)
    log2x = math.log(2,x)
    f_x = logx4 + log2x
    print(f"Gia tri can tim f(x) = {f_x:.2f}")
else :
      print("loi gia tri")
   