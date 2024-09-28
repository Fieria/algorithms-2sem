import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def calc(a, b, s):
    if s == "+":
        return a + b
    if s == "-":
        return a - b
    if s == "*":
        return a * b


def solve(s):
    nums = [int(s[i]) for i in range(0, len(s), 2)]
    ops = [s[i] for i in range(1, len(s), 2)]
    n = len(nums)

    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = nums[i]
        M[i][i] = nums[i]
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, m, M, ops)
    return M[0][n - 1]


def min_and_max(i, j, m, M, ops):
    maximum = float("inf") * (-1)
    minimum = float("inf")
    for k in range(i, j):
        a = calc(M[i][k], M[k + 1][j], ops[k])
        b = calc(m[i][k], M[k + 1][j], ops[k])
        c = calc(M[i][k], m[k + 1][j], ops[k])
        d = calc(m[i][k], m[k + 1][j], ops[k])
        maximum = max(maximum, a, b, c, d)
        minimum = min(minimum, a, b, c, d)
    return minimum, maximum


def write_to_file():
    f = open("input14.txt")
    s = f.readline()
    f.close()

    result = solve(s)
    file2 = open("output14.txt", "w+")
    file2.write(str(result))


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
