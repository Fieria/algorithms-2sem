import time
import tracemalloc
from collections import deque

t_start = time.perf_counter()
tracemalloc.start()


def bfs(n, nodes, v):
    colors = [-1] * n
    colors[v] = 0
    queue = deque([v])
    while queue:
        u = queue.popleft()
        for v in nodes[u]:
            if colors[v] == colors[u]:
                return 0
            if colors[v] == -1:
                colors[v] = (colors[u] + 1) % 2
                queue.append(v)
    return 1


def make_table_of_nodes(n, edges):
    nodes = [[] for v in range(n)]
    for i in range(len(edges)):
        v, w = [(int(i) - 1) for i in edges[i].split()]
        nodes[v].append(w)
        nodes[w].append(v)
    return nodes


def solve(n, edges):
    nodes = make_table_of_nodes(n, edges)
    return bfs(n, nodes, 0)


def write_to_file():
    f = open("input7.txt")
    n, m = [int(i) for i in f.readline().split()]
    edges = [f.readline() for _ in range(m)]
    f.close()

    answer = solve(n, edges)

    file2 = open("output7.txt", "w+")
    file2.write(str(answer) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
