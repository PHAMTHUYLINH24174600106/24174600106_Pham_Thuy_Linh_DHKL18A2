def tinh_trung_binh(*args):
    #kiem tra gia tri trong args
    tong = 0
    for i in args:
        tong = tong + i
    trung_binh = tong/len(args)
    return trung_binh

tinh_trung_binh(1,2,3,4,5,6,7,7,8,9,10)



list_ttsv = []
def nhap_thong_tin_sv(**kwargs):
    #kiem tra cac gia trị trong kwargs
    if kwargs["diem_tb"] >=7:
        kwargs["lop"] = "A1"
    elif kwargs["diem_tb"] >=4:
        kwargs["lop"] = "A2"
    else:
        kwargs["lop"] = "A3"
    list_ttsv.append(kwargs)

nhap_thong_tin_sv(ten="Trung", tuoi="18", diem_tb="5.0")



def tinh_tong_hai_so(a: int = 1, b: int = 2) -> float
    """
    Hàm tính toán nhập vào hai số a và b \n
    Trả về tổng hai số này
    """
    return a + b

tinh_tong_hai_so(4,5)

print("avc","ád",12,"ádasd",4,3,2,3,5)

sum()





