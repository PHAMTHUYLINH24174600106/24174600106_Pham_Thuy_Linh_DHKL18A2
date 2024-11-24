# câu lệnh vòng lặp while
n = 10
while n > 2: #True
    print(f"Chạy vòng lặp {n}")
    n = n + 1 

# vòng lặp while cũng hỗ trợ: break, continue và else
# Break
n = 10
while n > 2: 
    print(f"Chạy vòng lặp {n}")
    n = n + 1 
    if n == 66666:
        break
# Continue
n = 10
while n > 2: 
    n = n - 1 
    if n == 6:
        continue
    print(f"Chạy vòng lặp {n}")
# Else
n = 10
while n > 2: 
    print(f"Chạy vòng lặp {n}")
    n = n - 1 
    if n == 6:
        continue
else: 
    print("Chạy câu lệnh else")

# Tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng 20
n = 20
while True:
    for i in range(1,n):
        if n % i == 0 and i!=1 and i!=n:
            n = n - 1
            break
    else:
        break      
    if n < 1:
        break
print(f"Số nguyên tố là {n}")