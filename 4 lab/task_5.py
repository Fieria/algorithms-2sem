"""Эффективный алгоритм префикс функции"""
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def prefixFuncion(s):
    p = [0] * (len(s) + 1)  # массив длин наибольших бордеров для каждого префикса
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            p[i+1] = j+1
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j]
            else:
                p[i+1] = 0
                i += 1
    return p


def solve(s):  # форматирует результат prefixFuncion
    return " ".join([str(i) for i in prefixFuncion(s)[1:]])


def write_to_file():
    f = open("input5.txt")
    s = f.readline().rstrip()
    f.close()

    result = solve(s)

    file2 = open("output5.txt", "w+")
    file2.write(result)
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
