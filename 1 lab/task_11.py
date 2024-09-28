import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def solve(W, n, weights):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for j in range(1, n + 1): # j - сколько первых элементов weights можно брать
        for i in range(1, W+1): # i - вместимость рюкзака
            dp[j][i] = dp[j-1][i]
            if i >= weights[j - 1]:
                dp[j][i] = max(dp[j][i], dp[j-1][i - weights[j - 1]] + weights[j - 1])
    return dp[n][W]


def write_to_file():
    f = open("input11.txt")
    W, n = [int(i) for i in f.readline().split()]
    w = [int(i) for i in f.readline().split()]
    f.close()

    result = solve(W, n, w)
    file2 = open("output11.txt", "w+")
    file2.write(str(result))


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
