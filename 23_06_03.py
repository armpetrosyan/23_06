def is_sorted(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                store2 = a[j+1]
                a[j + 1] = a[j]
                a[j] = store2
    if ls == ls2:
        return True
    else:
        return False


ls = [1, 2, 3, 4, 5]
ls2 = []

for k in range(len(ls)):
    ls2.append(ls[k])


x = is_sorted(ls2)

print(x)
