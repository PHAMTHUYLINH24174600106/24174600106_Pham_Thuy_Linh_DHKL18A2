print("Hello World")

a = "Hello World"
b = 'Hello World'

c = 'Bạn A nói:"Abcd"'
c = "Bạn A nói:'Abcd'"

# kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó 
# truy cập sử dụng index (danh mục)

print(a[-9])

#[Start:stop:step]
# start: vị trí bắt đầu
# stop: vị trí kết thúc
# step: khoảng cách giữa các bước
print(a[1:7]) # lấy các giá trị từ start đến stop -1
print(a[:7])
print(a[1:])
print(a[:])
# mặc định của step luôn = 1
print(a[1:7:2])
print(a[:7:2])
print(a[1::2])
print(a[::2])
print(a[::-1])

print(range(5)) #0,1,2,3,4
range(1,5)
range(1,5,2)

for item in a:
    print(item)

# hàm đo độ dài kiểu dữ liệu tuần tự: len
print(len(a))

for i in range(len(a)):
    print(a[i])

# tính chất của kiểu dữ liệu chuỗi kí tự:
# - có thể truy cập
# - không thể chỉnh sửa
# - không thể sắp xếp

b = "Hello" + "world"
print(b)
n = int(input("Nhập vào số nguyên dương: "))
if n > 0:
    print("đã nhập đúng")

c =" "
for i in range(len(a)):
    if a[i] == "a":
        c = c + 1   

# phương thức trong xử lí chuỗi kí tự
a = "Hello world"
# các phương thức ktra(trả về cho mình true hoặc false)
# các phương thức này sẽ thường bắt đầu bằng chữ "is"

# kiểm tra chuỗi có phải alphanumeric(chỉ có kí tự số và chữ hay không)
print(a.isalnum())
# kiểm tra chuỗi có toàn số hay không (numeric)
print(a.isnumeric())
# kiểm tra chuỗi có toàn chữ hay không (character)
print(a.isalpha())
print(a.isascii())
# - kiểm tra chuỗi có phải kiểu số hay không
print(a.isdigit()) # số thông thường
print(a.isdecimal()) # số thập phân
#kiểm tra xem chuỗi có khoảng trống hay không
print(a.isspace())
# kiểm tra in hoa in thường
print(a.isupper())
print(a.islower())

# kiểm tra kí tự tồn tại trong chuỗi
print(a.find("llo"))
print(a.count("L"))
print(a.index("l"))



# phương thức biến đổi (các phương thức này trả về chuỗi kí tự mới, không thay đổi chuỗi ký tự ban đầu)
a = "Hello world"
# - xóa kí tự đầu và cuối của chuỗi
a_sua = a.strip()
a_sua = a.lstrip()
a_sua = a.rsplit()

# - thay thế ký tự bắt đầu
a_sua = a.replace("1","w")

# - biến đối viết hoa viết thường
a_sua = a.upper()
a_sua = a.lower()
a_sua = a.capitalize() # viết hoa ở chữ cái đầu tiên