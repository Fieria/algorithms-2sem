import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(k, root):
    if root is None or root.key == k:
        return root
    if k < root.key:
        return find(k, root.left)
    if k > root.key:
        return find(k, root.right)


def delete(node):
    if node is not None:
        parent = node.parent
        if parent.key < node.key:
            parent.right = None
        else:
            parent.left = None
        node.parent = None


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def solve(n, array, m, requests):
    answers = []
    nodes = []
    for i in range(n):
        nodes.append(Node(array[i][0]))
    for i in range(n):
        l_node_index = array[i][1] - 1
        r_node_index = array[i][2] - 1
        if l_node_index != -1:
            nodes[i].left = nodes[l_node_index]
            nodes[l_node_index].parent = nodes[i]
        if r_node_index != -1:
            nodes[i].right = nodes[r_node_index]
            nodes[r_node_index].parent = nodes[i]
    root = nodes[0]
    for k in requests:
        node = find(k, root)
        n -= count_nodes(node)
        delete(node)
        answers.append(n)
    return answers


def write_to_file():
    f = open("input9.txt")
    n = int(f.readline())
    array = [[int(i) for i in f.readline().strip().split()] for _ in range(n)]
    m = int(f.readline())
    requests = [int(i) for i in f.readline().strip().split()]
    f.close()

    answers = [str(el) for el in solve(n, array, m, requests)]
    file2 = open("output9.txt", "w+")
    file2.write(" ".join(answers) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
