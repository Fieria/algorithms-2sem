import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def explore(graph, visited, v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            explore(graph, visited, w)


def find(graph, visited, v):
    for w in graph[v]:
        visited[w] = True
    for w in graph[v]:
        explore(graph, visited, w)


def check(graph, n, v):
    visited = [False for _ in range(n)]
    find(graph, visited, v)
    return 'YES' if visited[v] else 'NO'


def make_graph(n, processes):
    ids = dict()
    for i in range(n):
        ids[processes[i][0]] = i
    graph = []
    for i in range(n):
        graph.append([ids[pr] for pr in processes[i][1:]])
    return graph


def solve(n, processes):
    graph = make_graph(n, processes)
    return [check(graph, n, i) for i in range(n)]


def write_to_file():
    file1 = open("input16.txt")
    n = int(file1.readline())
    processes = []
    for i in range(n):
        pr = file1.readline()
        processes.append([pr])
        processes[-1].extend([file1.readline() for _ in range(int(file1.readline()))])
        file1.readline()
    file1.close()

    answer = solve(n, processes)

    file2 = open("output16.txt", "w+")
    for el in answer:
        file2.write(el + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
