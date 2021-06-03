# Nhập vào một số nguyên dương n, và n số nguyên lần lượt là các phần tử
# trong dãy a.
# Hãy đưa ra một số nguyên là tổng tất cả các phần tử trong dãy đó.

n = (int)(input()) # so nguyen duong n
a = []  # list a

# nhap lan luot cac so nguyen
for i in range(n):
    a.append((int)(input()))
# tinh tong tat ca so da nhap vao list
Sum = 0
for i in range(n):
    Sum += a[i]
# in ra ket qua
print(Sum)