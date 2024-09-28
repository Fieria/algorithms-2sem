import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()
infinity = float("inf")


def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    array1 = array[p: q + 1] + [infinity]
    array2 = array[q + 1: r + 1] + [infinity]
    i, j = 0, 0
    for k in range(p, r + 1):
        if array1[i] <= array2[j]:
            array[k] = array1[i]
            i += 1
        else:
            array[k] = array2[j]
            j += 1


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)
        return array
    return array


def solve(A, B, n):
    sorted_A = [i for i in merge_sort(A, 0, n - 1)]
    sorted_B = [i for i in merge_sort(B, 0, n - 1)]
    return sum([sorted_A[i] * sorted_B[i] for i in range(n)])


def write_to_file():
    f = open("input3.txt")
    n = int(f.readline())
    A = [int(i) for i in f.readline().split()]
    B = [int(i) for i in f.readline().split()]
    f.close()

    result = solve(A, B, n)
    file2 = open("output3.txt", "w+")
    file2.write(str(result))


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
