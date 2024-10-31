diem_chuyen_can = float(input("nhập số điểm : "))
diem_giua_ki = float(input("nhập số điểm : "))
diem_cuoi_ki = float(input("nhập số điểm : "))
diem_trung_binh = (diem_cuoi_ki + diem_giua_ki + diem_chuyen_can)/3
if diem_trung_binh >= 9 : 
    print("ban dat loai A")
if diem_trung_binh < 9 and diem_trung_binh >= 7 :
    print("ban dat loai B")
if diem_trung_binh < 7 and diem_trung_binh >= 5 :
    print("ban dat loai C")
if diem_trung_binh < 5 :
    print("ban dat loai D")   

   
