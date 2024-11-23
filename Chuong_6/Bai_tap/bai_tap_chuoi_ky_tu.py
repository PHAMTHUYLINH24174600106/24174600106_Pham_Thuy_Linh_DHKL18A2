# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4
chuoi_ky_tu = input("Nhập vào chuỗi ký tự: ")
so_tu = chuoi_ky_tu.split()
print("Số từ có trong chuỗi là:", len(so_tu))


# Bài 2: Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”
chuoi_ky_tu = input("Nhập vào chuỗi ký tự: ")
tra_ve = " ".join(chuoi_ky_tu.split())
print(f"Ket qua tra ve la:{tra_ve}")


# Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”
ho_ten = input("Nhập vào họ tên đầy đủ: ").strip()
danh_sach_ten = ho_ten.split()
ho = danh_sach_ten[0]
ten = danh_sach_ten[-1]
print(f"Họ: {ho}, Tên: {ten}")


# Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự đặc biệt (Không là số, không là chữ) trong chuỗi
chuoi = input("Nhập vào chuỗi ký tự: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():  
        dem_chu += 1
    elif ky_tu.isdigit():  
        dem_so += 1
    else:  
        dem_ky_tu_dac_biet += 1
print(f"Số ký tự là chữ: {dem_chu}")
print(f"Số ký tự là số: {dem_so}")
print(f"Số ký tự là ký tự đặc biệt: {dem_ky_tu_dac_biet}")


# Bài 5: Viết chương trình nhập vào chuỗi ký tự, đếm xem có bao nhiêu chữ cái viết hoa, bao nhiêu chữ cái viết thường
chuoi_ky_tu = input("Nhập vào chuỗi ký tự: ")
viet_hoa = 0
viet_thuong = 0
for ky_tu in chuoi_ky_tu:
    if ky_tu.isupper(): 
        viet_hoa += 1
    elif ky_tu.islower(): 
        viet_thuong += 1
print(f"Số chữ cái viết hoa: {viet_hoa}")
print(f"Số chữ cái viết thường: {viet_thuong}")

# Bài 6:  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
chuoi = input("Nhập vào chuỗi ký tự: ").strip()
if chuoi.startswith("-") and chuoi[1:].isdigit():
    print("Chuỗi nhập vào là một số âm.")
else:
    print("Chuỗi nhập vào không phải là một số âm.")


# Bài 7: Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
chuoi = input("Nhập vào chuỗi ký tự: ").strip()
if chuoi.count('.') == 1 and chuoi.replace('.', '', 1).replace('-', '', 1).isdigit():
    print("Chuỗi nhập vào là một số thập phân.")
else:
    print("Chuỗi nhập vào không phải là một số thập phân.")


# Bài 8: Viết chương trình nhập vào 2 xâu ký tự str_1 và str_2. Kiểm tra xem str_2 có nằm trong str_1 hay không và ngược lại
str_1 = input("Nhập vào chuỗi str_1: ")
str_2 = input("Nhập vào chuỗi str_2: ")
if str_2 in str_1:
    print(f"'{str_2}' có nằm trong '{str_1}'.")
else:
    print(f"'{str_2}' không có trong '{str_1}'.")
if str_1 in str_2:
    print(f"'{str_1}' có nằm trong '{str_2}'.")
else:
    print(f"'{str_1}' không có trong '{str_2}'.")


# Bài 9: Viết chương trình nhập vào một chuỗi ký tự nhị phân 0 và 1. Kiểm tra xem chuỗi có phải số nhị phân không và chuyển đổi sang số thập phân
# Ví dụ: Nhập vào: “0010”
#              Trả về: “0010 la so nhi phan, chuyen sang thap phan: 2”
chuoi = input("Nhập vào chuỗi ký tự nhị phân: ").strip()
nhi_phan = True  
for ky_tu in chuoi:
    if ky_tu not in '01':  
        nhi_phan = False
        break
if nhi_phan:
    thap_phan = int(chuoi, 2)
    print(f"{chuoi} là số nhị phân, chuyển sang thập phân: {thap_phan}")
else:
    print(f"{chuoi} không phải là số nhị phân.")


# Bài 10: Viết chương trình nhập vào một chuỗi ký tự, trả về kết quả chuỗi mới sau khi dồn tất cả số sang bên trái
# Ví dụ: Nhập vào: “Xsn61ssakdu271626s  1231  12”
#              Trả về: “61271626123112Xsnssakdus   ”
chuoi = input("Nhập vào chuỗi ký tự: ").strip()
so = ''
khong_phai_so = ''
for ky_tu in chuoi:
    if ky_tu.isdigit(): 
        so += ky_tu
    else:
        khong_phai_so += ky_tu
ket_qua = so + khong_phai_so
print(f"Kết quả: {ket_qua}")

