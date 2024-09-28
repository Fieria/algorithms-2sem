import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


# nodes - список смежности
# visited - список посещенных вершин

def explore(nodes, visited, v):  # найти все вершины, достижимые из v
    visited[v] = True
    for w in nodes[v]:
        if not visited[w]:
            explore(nodes, visited, w)


def dfs(nodes):  # обход в глубину
    visited = [False for v in range(len(nodes))]
    cc = 1  # первая компонента связности
    for v in range(len(nodes)):
        if not visited[v]:
            explore(nodes, visited, v)
            cc += 1
    return cc - 1


def make_table_of_nodes(n, edges):
    nodes = [[] for v in range(n)]
    for i in range(len(edges)):
        v, w = [(int(i) - 1) for i in edges[i].split()]
        nodes[v].append(w)
        nodes[w].append(v)
    return nodes


def solve(n, edges):
    nodes = make_table_of_nodes(n, edges)
    return dfs(nodes)


def write_to_file():
    f = open("input2.txt")
    n, m = [int(i) for i in f.readline().split()]
    edges = [f.readline() for _ in range(m)]
    f.close()

    answer = solve(n, edges)

    file2 = open("output2.txt", "w+")
    file2.write(str(answer) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
