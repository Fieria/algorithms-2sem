import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def solve(dist, n):
    infinity = float("inf")
    min_length = infinity
    path = []
    # перебираем все варианты, в какой вершине может начинаться гамильтонов путь
    for start in range(n):
        visited = [start]
        length = 0

        for _ in range(n - 1):
            curr_city = visited[-1]
            min_dist = float('inf')
            close_city = -1
            for city in range(n):
                if city not in visited and dist[curr_city][city] < min_dist:
                    min_dist = dist[curr_city][city]
                    close_city = city
            visited.append(close_city)
            length += min_dist
        if length < min_length:
            min_length = length
            path = visited
    return min_length, [x+1 for x in path]


def write_to_file():
    f = open("input16.txt")
    n = int(f.readline())
    dist = [[int(el) for el in f.readline().split()] for _ in range(n)]
    f.close()

    lenght, path = solve(dist, n)

    file2 = open("output16.txt", "w+")
    file2.write(str(lenght) + "\n")
    file2.write(f'{" ".join(str(x) for x in path)}')
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
