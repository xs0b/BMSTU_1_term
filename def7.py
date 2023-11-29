n = int(input("введите длину списка: "))
arr = [int(a) for a in input("Введите список через пробел: ").split()]
import statistics
print("Медиана равна: ", statistics.median(arr))

for i in range(n):
    k = 0
    for j in range(n):
        if i == j:
            pass
        if arr[i] < arr[j]:
            k += 1
    if k == (n // 2):
        print("Медиана равна:", arr[i])