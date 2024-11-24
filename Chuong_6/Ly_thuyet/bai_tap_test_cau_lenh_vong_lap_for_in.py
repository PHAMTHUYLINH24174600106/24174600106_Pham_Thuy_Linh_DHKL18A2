# in dãy số n
n = int(input("Nhập số nguyên dương n: "))
for i in range(n): # -> chuỗi chạy từ 0 đến n-1
    if i%2 == 1:
        print(i)
# in n các số fibonacci
a = 0
b = 1
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b
# tính tổng các số hạng từ 1 đến n
tong_s = 0
n = int(input("Nhập vào giá trị nguyên dương n: "))
for i in range ( n + 1 ):
    tong_s = tong_s + i 
    print(f"tong lan lap thu {i} = {tong_s}")
print(f"Tổng các số từ 1 đến n là: {tong_s}")

# tính giai thừa của số n (n!)
tich_p = 1
n = int(input("Nhập vào giá trị nguyên dương n: "))
for i in range ( n + 1 ):
    if i == 0:
        continue
    tich_p = tich_p * i 
print(f"Tích giai thừa số n là: {tich_p}")

# nhập vào 2 số a,b. Tìm ƯCLN của 2 số này
a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
so_nho_nhat = a
if b <= a:
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} là ước chung lớn nhất")
        break
    k = k - 1


# ktra số n có phải 1 số nguyên tố hay không
# số nguyên tố là số nguyên dương lớn hơn 1 và chỉ chia hết cho 1 và chính nó

n = int(input("Nhập vào số nguyên dương cần kiểm tra: "))
if n <= 1:
    print("Số này không phải là số nguyên tố")
else: 
    k = n 
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("Số này không phải là số nguyên tố")
            break
        k = k - 1
    else: 
        print("số này là số nguyên tố")



# S = 1 + 2 +...+n

# Nhập vào số n, tính tổng n số hạng dựa theo S
# S = 1 - 1/2 + 1/3 - 1/4 + ... +  ((-1)**n)*(1/n)
# 1/1 + (-1)*1/2 + (1)*(1/3) - (-1)*1/4 +....
# ((-1)**n)*(1/n)
# E((-1)**n)*(1/n)
