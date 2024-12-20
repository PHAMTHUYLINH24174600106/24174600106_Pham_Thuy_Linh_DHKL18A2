 #De_quy - Recursion - sự tái lặp

 #Ví dụ: Dãy fibonacci
 #0 + 1 = 1
 #1 + 1 = 2 ####
 #1 + 2 = 3
 #2 + 3 = 5
 #3 + 5 = 8
 #5 + 8 = 13
 #........
 #Số tiếp theo = số hiện tại + số trước đó
 #F1 = 2
 #F2 = 3
 #F3 = F1 + F2 = 2 + 3 = 5
 #F(n) = F(n-1) +F(n-2) => Đệ quy trên toán học

 #Đệ quy trong lập trình là các hàm có lời gọi chính nó
 #trong một hàm
def f():
    f()
#=> Hàm đệ quy hoạt động khhoong khác gì vòng lặp

f()

import sys
#Xem giới hạn số vòng đệ quy
sys.getrecursionlimit()
#Điều chỉnh giới hạn số vòng đệ quy
sys.setrecursionlimit(1000000)

#Yêu cầu khi viết đệ quy:
#1. Tham số của hàm đệ quy cần thay đổi sau mỗi lần lặp đệ quy
#2. Cần có điểm dừng cho lặp đệ quy

n = 10
while True:
    n = n + 1
    if n == 20:
        break

n = 10
def f(x):
    if x == 20:
        return x

    return f(x + 1)

#Lần 1: x = 10 if False -> f(x+1) x = 11
#Lần 2: x = 11 if False -> f(x+1) x = 12
#Lần 3: x = 12 if False -> f(x+1) x = 13
#...
#Lần 9: x = 19 if False -> f(x+1) x = 20
#Lần 10: x = 20 if True -> 20 trả về cho lần 9, hủy lần 10
#Lần 9: nhận f(x + 1) = 20 -> 20 trả về cho lần 8, hủy lần 9
#...
#Lần 2: nhận f(x + 1) = 20 -> 20 trả về cho lần 1, hủy lần 2
#Lần 1: nhận f(x + 1) = 20 -> trả về kết quả 20, hủy lần 1

#Bài tập Fibonacci
#In ra n số Fibonacci
n = int(input("Nhap vao so nguyen duong n: "))
#F(n) = F(n-1) + F(n-2)
def fibonacci(n):
    #n = 2 => F_2 = 1
    if n == 2:
        return 1
    #n = 1 => F_1 = 1
    if n == 1:
        return 1
    #n = 0 => F_0 = 0
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(n):
    print(fibonacci(i), end=" ")


#Bài tập về giai thừa n!
n = int(input("Nhap vao so nguyen duong n: "))
tich=1
for i in range(1,n+1):
    tich=tich*i
print(tich)

def giai_thua(x):
    if x == 1:
        return 1
    else:
        return x*giai_thua(x-1)

print(giai_thua(n))
#x*giai_thua(x-1)*giai_thua(x-1-1)*giai_thua(x-1-1-1)*....*1

#Hàm đếm countdown
n = 60
while True:
    print(n, end=" ")
    if n == 1:
        break
    else:
        n = n - 1

def countdown(x):
    print(x, end=" ")
    if x == 1:
        return x
    else:
        return countdown(x)


#Áp dụng đệ quy vào giải thuật
#Giải thuật sắp xếp trận (merge sort)
#a = [1, 5, 2, 4, 9, 3, 7, 8, 6]
#Sắp xếp lại dãy a theo thứ tự từ nhỏ đễn lớn
a = [1, 5, 2, 4, 9, 3, 7, 8, 6]

def merge(day_ben_trai, day_ben_phai):
    ket_qua = []
    while day_ben_trai != [] and day_ben_phai != []:
        if len(day_ben_trai) > 0 and len(day_ben_phai) > 0:
            if day_ben_trai[0] < day_ben_phai[0]:
                ket_qua.append(day_ben_trai[0])
                day_ben_trai = day_ben_trai[1:]
            else:
                ket_qua.append(day_ben_phai[0])
                day_ben_phai = day_ben_phai[1:]
        if len(day_ben_trai) == 0:
            ket_qua.append(day_ben_trai[0])
            break
        if len(day_ben_phai) == 0:
            ket_qua.append(day_ben_phai[0])
            break
    return ket_qua

def merge_sort(a):
    if len(a) <= 1:
        return a

    day_ben_trai = a[:len(a)//2]
    day_ben_phai = a[len(a)//2 :]
    sap_xep_trai = merge_sort(day_ben_trai)
    sap_xep_phai = merge_sort(day_ben_phai)
    return merge(sap_xep_trai, sap_xep_phai)

a_sap_xep = merge_sort(a)
print(a_sap_xep)
#Giải thuật sắp xếp nhanh (quick sort)

#Giải thuật backtracking
#Giải thuật nhánh cây lựa chno (decision tree)


