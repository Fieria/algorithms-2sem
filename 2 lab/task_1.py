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


# центрированный обход
def InOrderTraversal(root):
    if root is None:
        return []
    return [*InOrderTraversal(root.left), root.key, *InOrderTraversal(root.right)]


# прямой обход
def PreOrderTraversal(root):
    if root is None:
        return []
    return [root.key, *PreOrderTraversal(root.left), *PreOrderTraversal(root.right)]


# обратный обход
def PostOrderTraversal(root):
    if root is None:
        return []
    return [*PostOrderTraversal(root.left), *PostOrderTraversal(root.right), root.key]


def solve(n, array):
    dictionary = {}
    for i in range(n):
        dictionary[i] = Node(array[i][0])
    root = dictionary[0]
    for i in range(n):
        node = dictionary[i]
        l_node_index = array[i][1]
        r_node_index = array[i][2]
        if l_node_index != -1:
            node.left = dictionary[l_node_index]
        if r_node_index != -1:
            node.right = dictionary[r_node_index]

    in_order = " ".join([str(i) for i in InOrderTraversal(root)])
    pre_order = " ".join([str(i) for i in PreOrderTraversal(root)])
    post_order = " ".join([str(i) for i in PostOrderTraversal(root)])

    return in_order, pre_order, post_order


def write_to_file():
    f = open("input1.txt")
    n = int(f.readline())
    array = [[int(i) for i in f.readline().strip().split()] for _ in range(n)]
    f.close()

    a, b, c = solve(n, array)
    file2 = open("output1.txt", "w+")
    file2.write(a + "\n")
    file2.write(b + "\n")
    file2.write(c + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
