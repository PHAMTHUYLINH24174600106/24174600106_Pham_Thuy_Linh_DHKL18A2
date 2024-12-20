danh_sach_hang_hoa = []

def xem_danh_sach_hang_hoa():
    if not danh_sach_hang_hoa:
        print("Danh sách mặt hàng trống.")
    else:
        print(f"{'Mã hàng':<10}{'Tên hàng':<20}{'Đơn vị tính':<15}{'Đơn giá':<10}{'Số lượng':<10}{'Thành tiền':<15}{'Thuế VAT':<10}")
        for hang in danh_sach_hang_hoa:
            print(f"{hang['ma_hang']:<10}{hang['ten_hang']:<20}{hang['don_vi_tinh']:<15}{hang['don_gia']:<10}{hang['so_luong']:<10}{hang['thanh_tien']:<15}{hang['thue']:<10}")

def nhap_thong_tin_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá (số thực): "))
        so_luong = int(input("Nhập số lượng (số nguyên): "))
        thanh_tien = don_gia * so_luong
        thue = thanh_tien * 0.1  # Thuế VAT 10%

        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "thue": thue
        }

        danh_sach_hang_hoa.append(mat_hang)
        print("Đã thêm mặt hàng thành công.")
    except ValueError:
        print("Lỗi: Đơn giá và số lượng phải là số hợp lệ. Vui lòng nhập lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi; {e}")

# Hàm tìm kiếm và xóa mặt hàng
def tim_kiem_va_xoa_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng cần xóa: ")
        for hang in danh_sach_hang_hoa:
            if hang["ma_hang"] == ma_hang:
                danh_sach_hang_hoa.remove(hang)
                print(f"Đã xóa mặt hàng có mã {ma_hang}.")
                return
        print("Không tìm thấy mặt hàng.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Hàm tìm kiếm và chỉnh sửa mặt hàng
def tim_kiem_va_chinh_sua_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng cần chỉnh sửa: ")
        for hang in danh_sach_hang_hoa:
            if hang["ma_hang"] == ma_hang:
                hang["ten_hang"] = input("Nhập tên hàng mới: ")
                hang["don_vi_tinh"] = input("Nhập đơn vị tính mới: ")
                hang["don_gia"] = float(input("Nhập đơn giá mới (số thực): "))
                hang["so_luong"] = int(input("Nhập số lượng mới (số nguyên): "))
                hang["thanh_tien"] = hang["don_gia"] * hang["so_luong"]
                hang["thue"] = hang["thanh_tien"] * 0.1
                print(f"Đã chỉnh sửa mặt hàng có mã {ma_hang}.")
                return
        print("Không tìm thấy mặt hàng.")
    except ValueError:
        print("Lỗi: Đơn giá và số lượng phải là số hợp lệ. Vui lòng nhập lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Hàm sắp xếp danh sách mặt hàng theo tên
def sap_xep_theo_ten():
    try:
        danh_sach_hang_hoa.sort(key=lambda x: x["ten_hang"])
        print("Đã sắp xếp danh sách mặt hàng theo tên.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi sắp xếp: {e}")

# Menu chương trình
def menu():
    while True:
        print("\n--- Quản lý hàng hóa ---")
        print("1. Xem danh sách mặt hàng")
        print("2. Nhập thông tin mặt hàng")
        print("3. Tìm kiếm và xóa mặt hàng")
        print("4. Tìm kiếm và chỉnh sửa mặt hàng")
        print("5. Xem danh sách mặt hàng sắp xếp theo tên")
        print("6. Thoát chương trình")

        try:
            lua_chon = int(input("Nhập lựa chọn (1-6): "))
            if lua_chon == 1:
                xem_danh_sach_hang_hoa()
            elif lua_chon == 2:
                nhap_thong_tin_mat_hang()
            elif lua_chon == 3:
                tim_kiem_va_xoa_mat_hang()
            elif lua_chon == 4:
                tim_kiem_va_chinh_sua_mat_hang()
            elif lua_chon == 5:
                sap_xep_theo_ten()
            elif lua_chon == 6:
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập số từ 1 đến 6.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

# Chạy chương trình
menu()