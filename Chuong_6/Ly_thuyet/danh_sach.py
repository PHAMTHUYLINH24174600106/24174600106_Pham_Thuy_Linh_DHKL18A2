a = []
b = ["abc",1,5,6.7,[],(),{}]

a = 5
b = a
a = a + 1

print(a)
print(b)

# a = ["abc","def","ghijk", 1, 2, 3]
b = a
b[0] = "chuoi thay doi"
print(a)
print(b)

# phương thức sao lưu
a = ["abc","def","ghijk", 1, 2, 3]
b = a.copy()
b[0] = "chuoi thay doi"
print(a)
print(b)

# thay đổi giá trị trong danh sách
a = ["abc","def","ghijk", 1, 2, 3]
a[3] = 10
# a[1:4] = 5
a[1:4] = [6,7,8]
print(a)

# độ dài của danh sách
print(len(a))
# phương thức thêm và bớt
a.append("abca")
a.append([1,2,3]) #thêm các giá trị vào cuối danh sách
print(a)
# thêm nhiều phần tử vào danh sách
a.extend([1,2,3]) #thêm thành phần tử trong danh sách, chứ không phải danh sách trong danh sách như extend
print(a)
# xóa tất cẩ các phần tử trong danh sách 
a.clear()
# lấy phần tử cuối cùng trong danh sách, sử dụng và xóa phần tử đó khỏi danh sách
b = a.pop()
print(a)
print(b)
# xóa một phần tử trong chuỗi
a.remove("abc")
# thêm một phần tử vào ví trí xác định
a.insert(3,"baka")
# đếm số phần tử xuất hiện trong danh sách
a.count("abc")
# đảo ngược danh sách
a.reverse()
# trả về vị trí xuất hiện đầu tiên của phần tử trong danh sách
a.index(1)
# sắp xếp danh sách
a.sort(key=False,reverse=True)

b = [[1,2,[4,5,6]],"abc",[3,"rts",5]]
print(b[0][2][1])

# bài tập xử lí ma trận
matrix_a = [[0,1,2]
            [4,5,6]
            [7,8,9]]
n = 8
# nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n
print(matrix_a)
# BTVN: các phép tính cơ bản của ma trận với số và của ma trận với ma trận