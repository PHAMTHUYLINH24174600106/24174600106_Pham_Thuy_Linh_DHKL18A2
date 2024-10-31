# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
year = int(input("Nhập năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")


# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?
# Nhập tọa độ điểm M
import math
x = float(input("Nhập hoành độ x của điểm M: "))
y = float(input("Nhập tung độ y của điểm M: "))
a = float(input("Nhập hoành độ x của tâm I: "))
b = float(input("Nhập tung độ y của tâm I: "))
R = float(input("Nhập bán kính R: "))
khoang_cach = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if khoang_cach <= R:
    print(True)
else:
    print(False)


# 3. Viết chương trình tìm số lớn nhất trong 3 số bằng Python
so_1 = float(input("Nhập số thứ nhất: "))
so_2 = float(input("Nhập số thứ hai: "))
so_3 = float(input("Nhập số thứ ba: "))
so_lon_nhat = so_1  
if so_2 > so_lon_nhat:
    so_lon_nhat = so_2
if so_3 > so_lon_nhat:
    so_lon_nhat = so_3
print(f"Số lớn nhất là: {so_lon_nhat}")


# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.    
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải là bộ ba cạnh của tam giác.")
else:
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Tam giác vuông cân.")
        else:
            print("Tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông.")
    else:
        print("Tam giác thường.")


# 5. Viết chương trình kiểm tra một ký tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm. 
# Ký tự là bất kỳ được nhập từ bàn phím.
ky_tu = str(input("Nhập 1 ký tự chữ: "))
if ky_tu == "u" or ky_tu == "e" or ky_tu == "o" or ky_tu == "a" or ky_tu == "i":
    print("Đây là nguyên âm")
else:
    print("Đây là phụ âm")


# 6. Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
print("Chào mừng đến rạp chiếu phim !")
print("Vui lòng chọn một thể loại phim để xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
lua_chon = input("Nhập số tương ứng với thể loại phim bạn muốn xem: ")
if lua_chon == "1":
    print("Bạn đã chọn thể loại: Phim tình cảm.")
elif lua_chon == "2":
    print("Bạn đã chọn thể loại: Phim kinh dị.")
elif lua_chon == "3":
    print("Bạn đã chọn thể loại: Phim hoạt hình.")
elif lua_chon == "4":
    print("Bạn đã chọn thể loại: Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")


# 7. Viết chương trình giải hệ phương trình 2 ẩn:
# 	    a_1*x + b_1*y = c_1
#       a_2*x + b_2*y = c_2
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể
# Công thức Cramer2 dùng tính hệ phương trình 2 ẩn
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))
D = a1 * b2 - a2 * b1
if D == 0:
    D1 = c1 * b2 - c2 * b1
    D2 = a1 * c2 - a2 * c1
    if D1 == 0 and D2 == 0:
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
else:
    x = c1 * b2 - c2 * b1 / D
    y = a1 * c2 - a2 * c1 / D
    print(f"Nghiệm của hệ phương trình là: x = {x:.2f}, y = {y:.2f}")


# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm B là sinh viên loại giỏi, 
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.
diem = float(input("Nhập điểm của sinh viên: "))
if diem >= 9:
    loai = "A"
elif diem >= 8:
    loai = "B"
elif diem > 5:
    loai = "C"
elif diem == 5:
    loai = "D"
elif diem >= 2:
    loai = "E"
else:
    loai = "F"
print(f"Xếp loại: {loai}")


# 9. Tính cước taxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km
# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
# Loại xe chỉ nhập 4 hoặc 7.
# Nhập loại xe và khoảng cách
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
khoang_cach = float(input("Nhập khoảng cách (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))

# Khai báo biến giá cước
cuoc_taxi = 0

# Tính cước taxi dựa trên loại xe
if loai_xe == 4:
    # Cước cho xe 4 chỗ
    cuoc_mo_cua = 11000  # Giá mở cửa
    khoang_cach_mien_phi = 0.8
    cuoc_taxi += cuoc_mo_cua
    
    if khoang_cach > khoang_cach_mien_phi:
        khoang_cach -= khoang_cach_mien_phi  # Trừ đi km miễn phí
        if khoang_cach <= 20:
            cuoc_taxi += khoang_cach * 12100
        else:
            cuoc_taxi += 20 * 12100  # Cước cho 20 km đầu
            khoang_cach -= 20
            cuoc_taxi += khoang_cach * 10000  # Cước cho km từ 21 trở đi
elif loai_xe == 7:
    # Cước cho xe 7 chỗ
    cuoc_mo_cua = 13000  # Giá mở cửa
    khoang_cach_mien_phi = 0.8
    cuoc_taxi += cuoc_mo_cua
    
    if khoang_cach > khoang_cach_mien_phi:
        khoang_cach -= khoang_cach_mien_phi  # Trừ đi km miễn phí
        if khoang_cach <= 30:
            cuoc_taxi += khoang_cach * 14100
        else:
            cuoc_taxi += 30 * 14100  # Cước cho 30 km đầu
            khoang_cach -= 30
            cuoc_taxi += khoang_cach * 12000  # Cước cho km từ 31 trở đi
else:
    print("Loại xe không hợp lệ. Vui lòng nhập 4 hoặc 7.")

# Tính cước tiền chờ nếu loại xe hợp lệ
if loai_xe in [4, 7]:
    if thoi_gian_cho > 5:
        thoi_gian_cho -= 5  # 5 phút đầu miễn phí
        cuoc_taxi += thoi_gian_cho * 800  # Cước cho thời gian chờ

    # In ra tổng cước taxi
    print(f"Tổng cước taxi là: {cuoc_taxi} đồng.")


# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
# Nhập lương nhân viên
luong = float(input("Nhập lương nhân viên (triệu đồng): "))
thue = 0
luong_rong = 0
if luong > 15:
    thue = luong * 0.30
elif luong >= 7:
    thue = luong * 0.20
else:
    thue = luong * 0.10
luong_rong = luong - thue
print(f"Thuế thu nhập: {thue:.2f} triệu đồng")
print(f"Lương ròng: {luong_rong:.2f} triệu đồng")