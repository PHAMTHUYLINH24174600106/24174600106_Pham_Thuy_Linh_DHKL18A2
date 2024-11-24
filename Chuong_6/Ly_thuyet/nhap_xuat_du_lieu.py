print("Hello world")

chuoi_ky_tu = input ("Yeu cau nhap chuoi ky tu: ") #input luôn trả về kiểu dữ liệu là chuỗi kí tự
# print ("in ra man hinh",123,"va", chuoi_ky_tu)
print(f"In ra man hinh chuoi {chuoi_ky_tu}")

gia_tri_nhap = input ("yeu cau nhap vao so tu nhien: ") #mang kiểu ký tự
bien_so_nguyen = int(gia_tri_nhap) #ép kiểu số nguyên int
bien_so_thuc = float(gia_tri_nhap) #ép kiểu số thực float
bien_chuoi_ky_tu = str(gia_tri_nhap) #ép kiểu ký tự

bien_boolean = bool(bien_so_nguyen) #ép kiểu boolean: đúng sai true false
print(bien_boolean) # khi ép kiểu boolean cho kiểu ký tự luôn trả về true/false


bien_boolean = bool(int(input ("Yeu cau nhap cuoi ky tu: ")))