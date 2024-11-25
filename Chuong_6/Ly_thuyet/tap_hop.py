#set - tập hợp trong python
# tính chất của tập hơp
# - không có sắp xếp, không có thứ tự
# - những phần tử trong tập hợp là đặc hiệu (unique)
# - các giá trị trong set có thể thay đổi được, tuy nhiên nó chỉ có thể chứa các phần tử mang giá trị không đổi

list_a = ["fol","baa","baal"]

set_a = {1,2,3,"def"}
set_b = set(list_a) # => ("fol","baa","baal")

# kiếm tra số phần tử trong tập hợp
len(set_a)
# kiểm tra phần tử có tồn tại trong tập hợp không
2 in set_a # => trả về kiểu dữ liệu boolean: True
if 2 in set_a:
    print("2 co trong tap hop")

2 not in set_a # => trả về kiểu dữ liệu boolean: False
if 2 not in set_a:
    print("2 khong co trong tap hop")


# kiểm tra só sánh 2 tập hợp
tap_hop_a = {"a","b","c","d"}
tap_hop_b = {1,2,3,"a","b"}

# kiếm tra tập hợp A có phải tập hợp con của tập hợp B hay không?
tap_hop_a.issubset(tap_hop_b)
tap_hop_a < tap_hop_b
tap_hop_a <= tap_hop_b

#kiểm tra tập hợp A có phải tập hợp cha của B hay không?
tap_hop_a.issuperset(tap_hop_b)
tap_hop_a > tap_hop_b
tap_hop_a >= tap_hop_b

# kiểm tra xem 2 tập hợp có giao nhau hay không
tap_hop_a.isdisjoint(tap_hop_b) # => trả về boolean

tap_hop_a = {"a","b","c","d"}
tap_hop_b = {1,2,3,"a","b"}
tap_hop_c = {1,2,3,4,5,6}

#phép hợp tập hợp
tap_hop_tong = tap_hop_a.union(tap_hop_b)
tap_hop_tong = tap_hop_a.union(tap_hop_b).union(tap_hop_c)
tap_hop_tong = tap_hop_a | tap_hop_b | tap_hop_c

# phép lấy giao giữa các tập hợp
tap_hop_giao = tap_hop_a.intersection(tap_hop_b)
tap_hop_giao = tap_hop_a.intersection(tap_hop_b).intersection(tap_hop_c)
tap_hop_giao = tap_hop_a & tap_hop_a & tap_hop_c

# phép lấy phần tử trong một tập hợp mà không có trong các tập con hợp lại
tap_hop_khac = tap_hop_a.difference(tap_hop_b)
tap_hop_khac = tap_hop_a.difference(tap_hop_b).difference(tap_hop_c)
tap_hop_khac = tap_hop_a - tap_hop_b - tap_hop_c

# phép lấy hợp các phần có trong tập hợp này mà không có trong ttapaj hợp kia
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b)
tap_hop_khac_giao = tap_hop_a.symmetric_difference(tap_hop_b).symmetric_difference(tap_hop_c)
tap_hop_khac_giao = tap_hop_a ^ tap_hop_b ^ tap_hop_c





# chỉnh sửa tập hợp
tap_hop_a = {1,2,3}
tap_hop_b = {"a","b","b"}
# thêm phần tử vào a
tap_hop_a.add(9)
tap_hop_a.update(4,5,6) # tương tự với việc hợp 2 tập hợp
# a = 1
# b = 2
# a += b
tap_hop_a = tap_hop_a | tap_hop_b
tap_hop_a |= tap_hop_b

# giữ lại các phần tử là giao của 2 tập hợp
tap_hop_a.intersection_update(tap_hop_b)
tap_hop_a = tap_hop_a & tap_hop_b
tap_hop_a &= tap_hop_b

# giữ lại các phần tử có trong tập xét mà không có trong tập còn lại
tap_hop_a.difference_update(tap_hop_b)
tap_hop_a = tap_hop_a ^ tap_hop_b
tap_hop_a ^= tap_hop_b

# xóa phần tử trong tập hợp
# - xóa 1 phần tử
tap_hop_a.remove(2)
# - xóa nhiều phần tử trong một tâp hợp
tap_hop_a.difference_update({1,2})
# - xóa phần tử không gây lỗi
tap_hop_a.discard(2)
# lấy 1 phẩn tử bất kì ra để sử dụng và xóa phẩn tử này khởi tạo tập hợp
tap_hop_a.pop()
# xóa toàn bộ tập hợp
tap_hop_a.clear()


tap_hop = {"a","b","c","d","e"}
while tap_hop:
    a = tap_hop.pop()
    print(a)
    