print("Hello World")
a = 1
b = 1
di_hoc = 1
# if = 1
# else = 2

# giai phương trinh bac nhat ax + b = c
he_so_a = 1
he_so_b = 2
he_so_c = 3

bien_int = 3 #dinh dang int - kieu so nguyen: ...-1,0,1,2,...
bien_float = 4.5 #dinh dang float - kieu so thuc
bien_string = "Day la kieu ki tu" #dinh dang str (string) - kieu ki tu: abcdef

kieu_boolean_1 = True #dinh dang boo (boolean) - kieu lua chon True, False
kieu_boolean_2 = False 
#0 -> false
#1 -> true

kieu_none = None #dinh dang hai bao khong dinh dangg

kieu_list = [] #dinh dang list (danh sach) - kieu du lieu tuan tu dang danh sach [1,ab,...]
kieu_dictionary = {"khoa":"gia tri", "a":1} #dinh dang dict: tu dien
kieu_tuple = (1,2,"abc") #dinh dang tuple
kieu_set = {1,2,"abc"} #dinh dang set: tap hop


# Câu lệnh điều kiện
# 3 kiểu viết câu lệnh điều kiện
# câu lệnh if...: nếu (sử dụng với 1 điều kiện xét)
# câu lệnh if...else: nếu...thì ( sử dụng với 1 điều kiện xét và có điều kiện phủ định)
# câu lệnh if...elif...else: nếu đk này k xảy ra thì thực hiện câu lệnh tiếp theo (sử dụng với nhiều điều kiện cần xét )
# xử lí xoay quanh boolean (True,False)
1 > 2
1 < 2
1 >= 2
1 <= 2
1 != 2
"abc" == "123"
# trả về kết quả True hoặc False

# Đới với if khi xét điều kiện
# - Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện sai (False) thì câu lệnh của if sẽ bỏ qua

# Đối với if...else khi xét điều kiện
# Nếu điều kiện đúng (True) thì câu lệnh của if sẽ hoạt động
# Nếu điều kiện sai (False) thì câu lệnh của else sẽ phản hồi

# Đối với if...elif...else:
# - Nếu điều kiện của if đúng (True) thì câu lệnh của if sẽ hoạt động
# - Nếu điều kiện của if sai (False) thì xét tiếp điều kiện của elif
#   + Nếu điều kiện của elif đúng (True) thì câu lệnh của elif hoạt động
#   + Nếu điều kiện của elif sai (False) thì câu lệnh của else sẽ hoạt động
a = 0
if a > 0: 
    print("a la so duong")
elif a < 0:
    print("a la so am")
else:
    print("a la so 0")
print("Ket thuc chuong trinh")
# CÓ BAO NHIÊU ELIF CŨNG ĐƯỢC, NHƯNG CHỈ CÓ 1 IF VÀ 1 ELSE

#x thuộc khoảng (2,8) hop (14,24) => or
#x thuộc khoảng (2,8) hop (5,24)  => and
#dùng and 
#dùng or 
c = 1
(c > 2 and c <= 8) # tương đương với (2,8]
(c >= 14 and c <= 24) #[14,24)
if (c > 2 and c <= 8) or (c >= 14 and c <= 24):
    print("thoa man dieu kien")

# viết trong cấu trúc if
if c > 2 and c <= 8:
    print("Thoa man dieu kien")
elif c >= 14 and c <= 24: 
    print("Thoa man dieu kien")
else: 
    print("dieu kien khong thoa man")

# CÁC BƯỚC VẼ LƯU ĐỒ
# B1: nhập h và r
# B2: xét điều kiện h và r
#     nếu h > 0 hoặc r > 0 : Đúng
#     => chuyển sang B3
#     nếu sai
#     => chuyển đến B6
# B3: pi = 3.14
# B4: tính dttp, dtxp
# B5: In kq dttp, dtxq
# B6: end
