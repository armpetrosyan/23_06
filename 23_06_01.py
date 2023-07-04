def sorting(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                store2 = a[j+1]
                a[j + 1] = a[j]
                a[j] = store2
    return a


def merge(k, g):
    result = k + g
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j] > result[j + 1]:
                store1 = result[j+1]
                result[j + 1] = result[j]
                result[j] = store1
    return result


ls1 = [11, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4]

x = merge(sorting(ls1), sorting(ls2))

print(x)
