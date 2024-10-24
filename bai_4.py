t_gian = int(input("thoi gian su dung (s): "))
u = 220
i = 2.7 
cong_suat = u * i
cong_suat_tieu_thu = cong_suat * t_gian/(3600 * 1000)
tien = cong_suat_tieu_thu * 7000
if t_gian < 0 :
    print("Loi gia tri vui long nhap lai")
else :
    print(f"so tien phai tra : {tien}")    