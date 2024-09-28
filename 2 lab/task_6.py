import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


# центрированный обход
def InOrderTraversal(id, array):
    if id == -1:
        return []
    left_id = array[id][1]
    right_id = array[id][2]
    key = array[id][0]
    return [*InOrderTraversal(left_id, array), key, *InOrderTraversal(right_id, array)]


def solve(n, array):
    if not array:
        return "CORRECT"
    values = InOrderTraversal(0, array)
    for i in range(n-1):
        if values[i] >= values[i+1]:
            return "INCORRECT"
    return "CORRECT"


def write_to_file():
    f = open("input6.txt")
    n = int(f.readline())
    array = [[int(i) for i in f.readline().strip().split()] for _ in range(n)]
    f.close()

    answer = solve(n, array)
    file2 = open("output6.txt", "w+")
    file2.write(answer + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
