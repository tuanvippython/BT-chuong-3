# Sử dụng hàm split() để nhập dãy các số nguyên
danh_sach = input("Nhập dãy số nguyên: ").split()
danh_sach = [int(so_nguyen) for so_nguyen in danh_sach]

# Đếm số lần xuất hiện của từng số và lưu vào dictionary
for i in set(danh_sach):
    dem = danh_sach.count(i)
    print(f"({i},{dem})")





   