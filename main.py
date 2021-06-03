n = (int)(input())  # nhap vao mot so nguyen duong n
a = []  # array a

# nhap lan luot cac so nguyen n
for i in range(n):
    a.append((int)(input()))
result = ""
# binh phuong moi phan tu cua mang a
for i in range(n):
    a[i] = pow(a[i], 2)
    result += str(a[i]) + " " # chuyen sang dang chuoi

print(result.replace("," , " ")) # xoa dau "," va in ra