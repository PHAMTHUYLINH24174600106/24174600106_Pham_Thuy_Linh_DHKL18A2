# từ điển trong python
# - lưu trữ các kiểu dữ liệu khác nhau
# - có thể thay đổi các giá trị trong từ điển
# - có thể luuw các kiểu dữ liệu tuần tự khác tạo thành mạng lưới
# - không sử dụng chỉ mục mà thay vào đó là khác khóa(key)
# - tất cả các gá trị phải truy cập bằng khóa
tu_dien = {"abc":1,
           0:[1,2,3],
           (0,1):"ghijk"}
# khai báo từ điền
# - từ điển sử dụng ngoặc {} để khởi tạo
# - mỗi phần tử phải theo cặp khóa: giá trị
# - khóa trong từ điển phải là các giá trị không thể thay đổi
# - khóa không được giống nhau
list_a = [(0,"Hoang"),(1,"Cuong"),(2,"Lam")]
tu_dien_a = dict(list_a)
# từ điển trong pyhton có cách hoạt động giống như JSON
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["a"]
# lấy các giá trị khóa
tap_hop_khoa = tu_dien.keys()
# lấy danh sách giá trị
danh_sach_gia_tri = list(tu_dien.values())
# lấy danh sách các cặp khác giá trị
danh_sach_khoa_gia_tri = list(tu_dien.items())

# thêm giá trị vào trong từ điển
# cách 1
tu_dien = {"a": 1,
           "b": 2,
           "c": 3}
tu_dien["d"] = 4
# cách 2
tu_dien.update({"e":5})
print(tu_dien)

# xóa phần tử trong từ điển
tu_dien.clear() # xóa toàn bộ các giá trị
tu_dien.pop("b") # lấy ra và xóa phần tử tại khóa
tu_dien.popitem() # lấy ra và xóa các phần tử bất kì