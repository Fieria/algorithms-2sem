import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


# центрированный обход
def InOrderTraversal(id, array):
    left_id = array[id][1]
    right_id = array[id][2]
    key = array[id][0]
    if left_id == -1 and right_id == -1:
        return [array[id][0], True, array[id][0]]
    if left_id == -1:
        return [key, key <= array[right_id][0], InOrderTraversal(right_id, array)]
    if right_id == -1:
        return [InOrderTraversal(left_id, array), array[left_id][0] < key, key]
    res1 = InOrderTraversal(left_id, array)
    res2 = InOrderTraversal(right_id, array)
    return [res1[0], (res1[1] and res2[1] and (res1[2] < key <= res2[0])), res2[2]]


def solve(n, array):
    if not array:
        return "CORRECT"
    res = InOrderTraversal(0, array)
    if res[1]:
        return "CORRECT"
    return "INCORRECT"


def write_to_file():
    f = open("input7.txt")
    n = int(f.readline())
    array = [[int(i) for i in f.readline().strip().split()] for _ in range(n)]
    f.close()

    answer = solve(n, array)
    file2 = open("output7.txt", "w+")
    file2.write(answer + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
