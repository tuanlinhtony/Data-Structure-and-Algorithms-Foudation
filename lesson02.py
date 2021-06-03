# =============================== Num 2====================================================
# Nhập vào một số nguyên dương n, và n số nguyên lần lượt là các phần tử trong dãy a.
# Hãy thay đổi giá trị của mỗi phần tử thành bình phương của chính nó,
# sau đó in mảng đó ra màn hình (mỗi phần tử cách nhau bởi một khoảng trắng).
def powinlist():
    n = (int)(input()) # nhap vao mot so nguyen duong n
    a = [] # array a

    # nhap lan luot cac so nguyen n
    for i in range(n):
        a.append((int)(input()))
    powList = []
    # binh phuong moi phan tu cua mang a
    for i in range(n):
        powList.append(pow(a[i], 2) + " ")
    print(powList)
