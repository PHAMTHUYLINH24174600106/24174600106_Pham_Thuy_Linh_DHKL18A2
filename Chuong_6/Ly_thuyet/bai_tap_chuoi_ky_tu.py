# bài tập về chuỗi ký tự
# dạng thứ 1: áp dụng xử lý chuỗi ký tự bằng các phương thức có sẵn

# bài 1: nhận vào 1 chuỗi kí tự bất kỳ. đếm số ký tự trong chuỗi.
# cách 1:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
so_ky_tu_trong_chuoi = len(chuoi_nhap_vao)
print(f"Số ký tự trong chuỗi là {so_ky_tu_trong_chuoi}")
# cách 2: 
chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem + 1
print(f"Số ký tự trong chuỗi là {dem}")

# bài 2: nhập vào 1 chuỗi bất kỳ. xóa các khoảng trống ở đầu và cuỗi chuỗi
# cách 1:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
chuoi_sau_khi_xoa = chuoi_nhap_vao.strip()
print(f"chuoi sau khi xoa khoang trong la {chuoi_sau_khi_xoa}")
# cách 2:
chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
#"       chuoi nhap vao        "
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu

chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " " and kiem_tra_dau == False:
        continue
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau = chuoi_dao_nguoc_xu_ly_dau+ chu

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"chuoi sau khi xoa khoang trong la {chuoi_ket_qua}")

# bài 3: nhập vào 1 chuỗi bất kỳ, xóa tất cả các hoảng trống thừa trong chuỗi
# ví dụ:"   chuoi    nha ap    vao    "
chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}")

# BTVN: cách 2: xử lí chuỗi yêu cầu trên mà hông sử dụng các chuỗi ký tự
#Bài 3: Nhập vào một chuỗi bất kỳ. Xóa tất cả các khoảng trống thừa trong chuỗi
#Ví dụ: "     chuoi     nhap   vao         "
nhap_chuoi_vao = input("Nhập chuỗi của bạn vào :")
bien_luu_tam = []
bien_hien_tai = ""
for chu in nhap_chuoi_vao :
    if chu != " ":
        bien_hien_tai += chu
    else :
        if bien_hien_tai != "":
            bien_luu_tam += [bien_hien_tai]
            bien_hien_tai =""
if bien_hien_tai != "" :
    bien_luu_tam += bien_hien_tai 
chuoi_ket_qua = " ".join(bien_luu_tam)
print(f"Chuỗi của bạn là {chuoi_ket_qua}")



# dạng thứ 2: áp dụng kết hợp xử lý vòng lặp vầ xử lý chuỗi ký tự
# bài 1: nhập 1 chuỗi ký tự bất kỳ
# đếm xem có bao nhiêu ký tự là chữ, bao nhiêu ký tự la số và bao nhiêu ký tự đặc biệt
# isalpha(): kiểm tra chứ cái
# isdigit(): kiếm tra số

chuoi_nhap_vao = input("Nhập vào chuỗi bất kỳ: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu += 1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1

print(f"So chu:{dem_chu}")
print(f"So chu:{dem_so}")
print(f"So chu:{dem_ky_tu_dac_biet}")

# bài 2: nhập vào 1 số bất kỳ, ktra xem số này có phải là 1 số nguyên tố hay không
while True:
    n = input("Nhap vao so nguyen duong can kiem tra: ")
    if n.isdigit() == False : #7.32
        print("Gia tri nhap vao khong phai gia tri so nguyen duong")
    else:
        break

# bài 3: nhập vào 2 số thực bất kỳ. tính tổng 2 số thực đó
while True:
    a = input("Nhap vao so thuc a: ")
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if a.isdigit() == False:
        print("Gia tri nhap vao khong phai gia tri so")
    else:
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count("-")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("Gia tri nhap vao khong phai gia tri so")
        else:
            vi_tri_dau_gach = a.find("-")
            if vi_tri_dau_gach != 0:
                print("Gia tri nhap vao khong phai gia tri so")
            else:
                break

a = float(a)
b = float(b)
