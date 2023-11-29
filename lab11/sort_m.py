import time

def bubble_sort_f(list_i : list[int], n : int) -> tuple[float, int, list]:
    start = time.perf_counter_ns()
    k = 0
    for i in range(n - 1):
        flag = True
        for j in range(n - 1 - i):
            if list_i[j] >list_i[j + 1]:
                k += 1
                list_i[j], list_i[j + 1] = list_i[j + 1], list_i[j]
                flag = False
        if flag:
            break
    end = time.perf_counter_ns() - start
    return end, k, list_i
