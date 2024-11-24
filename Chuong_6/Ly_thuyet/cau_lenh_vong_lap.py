# Vòng lặp trong python
# vòng lặp có giới hạn (for)
# các kiểu dữ liệu tuần tự: string, list, tuple, set, dictionary
# range()
#for abc in range(10):
#     print(abc)
# range(10) -> 1,2,...,9
# range khi truyền giá trị mặc định yêu cầu phải là giá trị nguyên dương
# các giá trị trong range sẽ chạy từ - đến  n-1

# khi sd vòng lặp nên kết hợp sử dụng với các câu lệnh điều kiện
# (khi sd vòng lặp nên có mục đích rõ ràng)

# trong python, vòng lặp cung cấp cho người dùng 3 công cụ: break, continue, else
# break: phá vỡ vòng lặp ngay lập tức, tại lần lặp gặp break
for i in range (10):
    if i == 4:
        break
    print(i)
# continue: vòng lặp sẽ bỏ qua lần lặp mà ở đấy xuất hiện continue
for i in range (10):
    if i == 4:
        continue
    print(i)
# else: vòng lặp sẽ chạy các câu lệnh xử lí của else trong những trường hợp vòng lặp không gặp break
for i in range (10):
    if i == 4:
        break
    print(i)
else:
    print("Chay cau lenh else")
# vòng lặp không giới hạn (while)
