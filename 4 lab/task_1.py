"""Наивный поиск подстроки в строке"""
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def FindPatternNaive(p, t):  # возвращает индексы вхождения строки p в строку t
    result = []
    for i in range(len(t) - len(p) + 1):
        if AreEqual(t[i: i + len(p)], p):
            result.append(i)
    return [i + 1 for i in result]  # увеличиваем каждый индекс на 1, тк нумерация с единицы


def AreEqual(s1, s2):  # проверяет, равны ли строки
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def solve(p, t):  # находит вхождения строки p в строку t
    result = FindPatternNaive(p, t)
    return len(result), result


def write_to_file():
    f = open("input1.txt")
    p = f.readline().rstrip()
    t = f.readline().rstrip()
    f.close()

    n, indexes = solve(p, t)

    file2 = open("output1.txt", "w+")
    file2.write(str(n) + "\n")
    file2.write(" ".join([str(i) for i in indexes]) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
