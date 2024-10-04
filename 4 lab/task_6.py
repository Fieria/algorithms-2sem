"""Z-функция"""
"""для каждого суффикса вычисляет длину максимального префикса, совпадающего с префиксом всей строки"""
import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def z_function(s):
    values = []
    for j in range(len(s)):
        i = 0
        max_value_of_z_function = 0
        while j < len(s) and s[i] == s[j]:
            max_value_of_z_function += 1
            i += 1
            j += 1
        values.append(max_value_of_z_function)
    return values[1:]


def solve(s):  # форматирует результат z_function
    return " ".join([str(i) for i in z_function(s)])


def write_to_file():
    f = open("input6.txt")
    s = f.readline().rstrip()
    f.close()

    result = solve(s)

    file2 = open("output6.txt", "w+")
    file2.write(result)
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))



