#Bài 1: Nhập vào số nguyên dương n.
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1, i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)

#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    so = input(f"Nhap gia tri so thu {i + 1}: ")
    if so.isdigit() == False:
        print("Yeu cau nhap vao so!!")
    else:
        so = float(so)
        break
ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")

#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần
while True:
    try:
        n = int(input("Nhập vào số nguyên dương n: "))
        if n > 0:
            break 
        else:
            print("Số vừa nhập không phải là số nguyên dương. Vui lòng thử lại!")
    except ValueError:
        print("Vui lòng nhập một số nguyên!")
A = []
B = []
for i in range(n-1, -1, -1):
    if i % 2 != 0:
        A.append(i) 
    else:
        B.append(i)  
print(f"Danh sách A (số lẻ):{A}")
print(f"Danh sách B (số chẵn):{B}")

#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
m = int(input("Nhap vao so cot cua ma tran m = "))
n = int(input("Nhap vao so hang cua ma tran n = "))
#0 ... m
#.     .
#.     .
#.     .
#n ... 0
ma_tran_a = [[0,0,0], 
             [0,0,0],
             [0,0,0]]
ma_tan_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)

ma_tran_a = [[0]*m]*n #=>[[0,0,0,0,....,m],....]
print(ma_tran_a)

#Bài 5: Viết chương trình nhập vào n. Sinh ra ma trận đơn vị I kích cỡ n*n
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
n = int(input("Nhap vao n = "))
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)

#Bài 6: Viết chương trình nhập vào ma trận A kích cỡ m*n và in ra màn hình
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
print(f"Nhập các phần tử của ma trận {m}x{n}, mỗi phần tử cách nhau bởi dấu cách:")
A = []
for i in range(m):
    while True:
        try:
            hang = list(map(float, input(f"Nhập hàng {i + 1}: ").split()))
            if len(hang) == n:
                A.append(hang)
                break
            else:
                print(f"Vui lòng nhập đúng {n} phần tử!")
        except ValueError:
            print("Vui lòng nhập các số hợp lệ!")
print("Ma trận A là:")
for hang in A:
    print(" ".join(map(str, hang)))

#Bài 7: Viết chương trình đảo vị trí hai hàng i, j của ma trận A kích cỡ m*n
i = int(input("Nhap vao hang i "))
j = int(input("Nhap vao hang j "))
[[1, 0, 0, 0],[0, 1, 0 ,0],[0, 0, 1, 0],[0, 0, 0, 1]]
temp = ma_tran_don_vi[i]
ma_tran_don_vi[i] = ma_tran_don_vi[j]
ma_tran_don_vi[j] = temp
print(ma_tran_don_vi)

#Bài 8: Viết chương trình đảo vị trí hai cột i, j của ma trận A kích cỡ m*n
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))
A = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    A.append(hang)
i = int(input(f"Nhập chỉ số cột thứ nhất (từ 0 đến {n-1}): "))
j = int(input(f"Nhập chỉ số cột thứ hai (từ 0 đến {n-1}): "))
print("\nMa trận trước khi đảo:")
for hang in A:
    print(hang)
for hang in A:
    hang[i], hang[j] = hang[j], hang[i]
print("\nMa trận sau khi đảo:")
for hang in A:
    print(hang)

#Bài 9: Viết chương trình nhập vào hai ma trận A, B có cùng kích thước.
#Tính:
# - Tổng hai ma trận A, B
# - Hiệu hai ma trận A, B
# - Tích của ma trận A với số k nhập từ bàn phím
# - Tích hai ma trận A, B
# - Ma trận đối xứng của ma trận A
n = int(input("Nhập kích thước ma trận (n x n): "))
print("Nhập ma trận A:")
A = []
for i in range(n):
    hang = list(map(int, input(f"Hàng {i + 1}: ").split()))
    A.append(hang)
print("Nhập ma trận B:")
B = []
for i in range(n):
    hang = list(map(int, input(f"Hàng {i + 1}: ").split()))
    B.append(hang)
tong = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    tong.append(hang)
hieu = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] - B[i][j])
    hieu.append(hang)
k = int(input("Nhập số k để nhân với ma trận A: "))
tich_k_A = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[i][j] * k)
    tich_k_A.append(hang)
tich_A_B = []
for i in range(n):
    hang = []
    for j in range(n):
        tong = 0
        for k in range(n):
            tong += A[i][k] * B[k][j]
        hang.append(tong)
    tich_A_B.append(hang)
doi_xung_A = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(A[j][i])
    doi_xung_A.append(hang)
print("\nTổng hai ma trận A và B:")
for hang in tong:
    print(hang)
print("\nHiệu hai ma trận A và B:")
for hang in hieu:
    print(hang)
print(f"\nTích của ma trận A với số k ({k}):")
for hang in tich_k_A:
    print(hang)
print("\nTích hai ma trận A và B:")
for hang in tich_A_B:
    print(hang)
print("\nMa trận đối xứng của ma trận A:")
for hang in doi_xung_A:
    print(hang)



#Bài 10: Lập một danh sách với n sinh viên bao gồm thông tin tên và điểm tổng kết cuối năm của các sinh viên đó
#thong_tin_sinh_vien = {"Hung": 4.0}
#ds_sinh_vien = [{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0},{"Hung": 4.0}]
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)


#Bài 11: Viết lệnh in danh sách sinh viên ở bài 10. Có dạng:
#Ten    Diem
#Dung   10.0
#Quang  5.3
#Trang  7.5
#In danh sach sinh vien
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")

#Bài 12: Viết lệnh xóa thông tin của sinh viên trong danh sách sinh viên ở bài 10 ứng với tên được nhập vào bàn phím
ten_xoa = input("Nhap ten sinh vien can xoa: ")
xoa_thanh_cong = False
for sinh_vien in ds_sinh_vien:
    if ten_xoa in sinh_vien:
        ds_sinh_vien.remove(sinh_vien)
        xoa_thanh_cong = True
        break
if xoa_thanh_cong:
    print(f"Da xoa thong tin sinh vien co ten: {ten_xoa}")
else:
    print(f"Khong tim thay sinh vien co ten: {ten_xoa}")
print("\nDanh sach sinh vien sau khi xoa:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")

#Bài 13: Viết lệnh thêm một sinh viên vào danh sách sinh viên ở bài 10. Với điều kiện:
# - Nếu tên sinh viên đã tồn tại, thông báo: "Thông tin sinh viên đã tồn tại"
# - Nếu chưa có sinh viên này, thông báo: "Đã thêm sinh viên"
ten_them = input("Nhap ten sinh vien can them: ")
diem_them = float(input("Nhap diem sinh vien can them: "))
sinh_vien_ton_tai = False
for sinh_vien in ds_sinh_vien:
    if ten_them in sinh_vien:
        sinh_vien_ton_tai = True
        break
if sinh_vien_ton_tai:
    print("Thong tin sinh vien da ton tai")
else:
    thong_tin_sinh_vien_moi = {ten_them: diem_them}
    ds_sinh_vien.append(thong_tin_sinh_vien_moi)
    print("Da them sinh vien")
print("\nDanh sach sinh vien sau khi them:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")

#Bài 14: Viết lệnh sửa thông tin của một sinh viên ở bài 10 ứng với tên được nhập vào bàn phím
ten_sua = input("Nhap ten sinh vien can sua: ")
sinh_vien_ton_tai = False
for sinh_vien in ds_sinh_vien:
    if ten_sua in sinh_vien:
        sinh_vien_ton_tai = True
        diem_moi = float(input(f"Nhap diem moi cho sinh vien {ten_sua}: "))
        sinh_vien[ten_sua] = diem_moi
        print(f"Da sua thong tin sinh vien {ten_sua}.")
        break
if not sinh_vien_ton_tai:
    print(f"Khong tim thay sinh vien co ten: {ten_sua}")
print("\nDanh sach sinh vien sau khi sua:")
print("Ten\tDiem")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten}\t{diem}")

#Bài 15: Viết một chương trình quản lý một danh sách sinh viên.
# Danh sách sinh viên chứa các thông tin:
# - "Mã sinh viên"
# - "Họ đệm"
# - "Tên"
# - "Điểm toán"
# - "Điểm lý"
# - "Điểm hóa"
# - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
# Thiết kế chương trình quản lý có menu như sau:
# 1. Xem danh sách sinh viên
# 2. Nhập thông tin sinh viên mới vào danh sách
# 3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên
# 4. Xóa thông tin sinh viên ứng với mã sinh viên
# 5. Thoát chương trình
ds_sinh_vien = []
while True:
    print("MENU:")
    print("1. Xem danh sách sinh viên")
    print("2. Nhập thông tin sinh viên mới vào danh sách")
    print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print("5. Thoát chương trình")
    lua_chon = input("Nhap lua chon ma ban muon su dung: ")
    if lua_chon.isdigit() == False:
        print("Yeu cau nhap lai")
    else:
        lua_chon = int(lua_chon)
        if lua_chon == 1:
            print("Xem danh sách sinh viên")
            print("ma_sinh_vien","\t","ho_dem", "\t", "ten", "\t", "diem_toan", "\t", "diem_ly", "\t", "diem_hoa", "\t", "diem_tb")
            for sv in ds_sinh_vien:
                print(sv["ma_sinh_vien"],"\t",sv["ho_dem"], "\t", sv["ten"], "\t", sv["diem_toan"], "\t", sv["diem_ly"], "\t", sv["diem_hoa"], "\t", sv["diem_tb"])
        elif lua_chon == 2:
            # Danh sách sinh viên chứa các thông tin:
            # - "Mã sinh viên"
            # - "Họ đệm"
            # - "Tên"
            # - "Điểm toán"00     
            # - "Điểm lý"
            # - "Điểm hóa"
            # - "Điểm trung bình" được tính từ 3 điểm toán, lý, hóa
            print("Nhập thông tin sinh viên mới vào danh sách")
            #Cách 1: yêu cầu nhập vào số lượng sinh viên cần thêm
            # n = input("Nhap vao so sinh vien can cap nhap: ")
            # #thêm kiểm tra int
            # n = int(n)
            # for sv in range(n):
            #     sinh_vien = {"ma_sinh_vien": "",
            #                 "ho_dem": "",
            #                 "ten": "",
            #                 "diem_toan": 0.0,
            #                 "diem_ly": 0.0,
            #                 "diem_hoa": 0.0,
            #                 "diem_tb": 0.0,
            #                 }
            #     print(f"Nhap sinh vien thu {sv + 1}")
            #     sinh_vien['ma_sinh_vien'] = input("Nhap ma sinh vien: ")
            #     sinh_vien['ho_dem'] = input("Nhap ho dem: ")
            #     sinh_vien['ten'] = input("Nhap ten: ")
            #     #Thêm kiểm tra nhập float
            #     sinh_vien['diem_toan'] = float(input("Nhap diem toan: "))
            #     sinh_vien['diem_ly'] = float(input("Nhap diem ly: "))
            #     sinh_vien['diem_hoa'] = float(input("Nhap diem hoa: "))
            #     sinh_vien["diem_tb"] = (sinh_vien["diem_toan"] + sinh_vien["diem_ly"] + sinh_vien['diem_hoa'])/3
            #     ds_sinh_vien.append(sinh_vien)
            
            # print("Hoan thanh nhap danh sach sinh vien")
            #Cách 2: Cho phép người dùng nhập đến khi nào chán thì thôi
            while True:
                sinh_vien = {"ma_sinh_vien": "",
                            "ho_dem": "",
                            "ten": "",
                            "diem_toan": 0.0,
                            "diem_ly": 0.0,
                            "diem_hoa": 0.0,
                            "diem_tb": 0.0,
                            }
                sinh_vien['ma_sinh_vien'] = input("Nhap ma sinh vien: ")
                sinh_vien['ho_dem'] = input("Nhap ho dem: ")
                sinh_vien['ten'] = input("Nhap ten: ")
                #Thêm kiểm tra nhập float
                sinh_vien['diem_toan'] = float(input("Nhap diem toan: "))
                sinh_vien['diem_ly'] = float(input("Nhap diem ly: "))
                sinh_vien['diem_hoa'] = float(input("Nhap diem hoa: "))
                sinh_vien["diem_tb"] = (sinh_vien["diem_toan"] + sinh_vien["diem_ly"] + sinh_vien['diem_hoa'])/3
                ds_sinh_vien.append(sinh_vien)
                
                n = input("Ban co muon nhap them sinh vien nua khong? Y/N")
                if n.capitalize() != 'Y':
                    break
        elif lua_chon == 3:
            print("Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
            n = input("Nhap vao ma sinh vien muon sua: ")
            index = -1
            if len(ds_sinh_vien) == 0:
                print("Dang sach rong")
            else:
                for i in range(len(ds_sinh_vien)):
                    if ds_sinh_vien[i]["ma_sinh_vien"] == n:
                        print("Sinh vien co ton tai")
                        index = i
                        break
                else:
                    print("Sinh vien khong ton tai")
                
                if index != -1:
                    print("Sua thong tin sinh vien:")
                    ds_sinh_vien[index]['ma_sinh_vien'] = input("Nhap ma sinh vien: ")
                    ds_sinh_vien[index]['ho_dem'] = input("Nhap ho dem: ")
                    ds_sinh_vien[index]['ten'] = input("Nhap ten: ")
                    #Thêm kiểm tra nhập float
                    ds_sinh_vien[index]['diem_toan'] = float(input("Nhap diem toan: "))
                    ds_sinh_vien[index]['diem_ly'] = float(input("Nhap diem ly: "))
                    ds_sinh_vien[index]['diem_hoa'] = float(input("Nhap diem hoa: "))
                    ds_sinh_vien[index]["diem_tb"] = (ds_sinh_vien[index]["diem_toan"] + ds_sinh_vien[index]["diem_ly"] + ds_sinh_vien[index]['diem_hoa'])/3
        elif lua_chon == 4:
            print("Xóa thông tin sinh viên ứng với mã sinh viên")
            n = input("Nhap vao ma sinh vien muon xoa: ")
            index = -1
            if len(ds_sinh_vien) == 0:
                print("Dang sach rong")
            else:
                for i in range(len(ds_sinh_vien)):
                    if ds_sinh_vien[i]["ma_sinh_vien"] == n:
                        print("Sinh vien co ton tai")
                        index = i
                        break
                else:
                    print("Sinh vien khong ton tai")
                    
                if index != -1:
                    ds_sinh_vien.remove(ds_sinh_vien[index])   
                    print("Tien hanh xoa sinh vien thanh cong")
        elif lua_chon == 5:
            print("Thoat chuong trinh")
            break
        else:
            print("Yeu cau nhap lai")



