# Nhập dãy số nguyên từ bàn phím
x = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()
danh_sach = [int(num) for num in x]

# Sắp xếp dãy số theo thứ tự tăng dần
danh_sach.sort()

# In ra dãy số đã sắp xếp
print("Dãy số đã sắp xếp theo thứ tự tăng dần: ", danh_sach)
