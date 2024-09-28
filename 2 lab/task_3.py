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
    elif k < root.key:
        if root.left is not None:
            return find(k, root.left)
        return root
    elif k > root.key:
        if root.right is not None:
            return find(k, root.right)
        return root


def insert(k, root):
    p = find(k, root)
    if p is not None and p.key != k:
        new_node = Node(k)
        new_node.parent = p
        if k < p.key:
            p.left = new_node
        else:
            p.right = new_node


def tree_min(x):
    while x.left is not None:
        x = x.left
    return x


def tree_max(x):
    while x.right is not None:
        x = x.right
    return x


def next(P):
    if P.right:
        return tree_min(P.right)
    return right_ancestor(P)


def right_ancestor(P):
    if P.key < P.parent.key:
        return P.parent
    return right_ancestor(P.parent)


def find_min_bigger_than_x(x, root):
    biggest = tree_max(root)
    if biggest.key <= x:
        return 0
    N = find(x, root)
    while N.key <= x:
        N = next(N)
    return N.key


def solve(array):
    answer = []
    root = Node(int(array[0].split()[1]))
    for s in array[1:]:
        s = s.split()
        if s[0] == "+":
            insert(int(s[1]), root)
        else:
            answer.append(find_min_bigger_than_x(int(s[1]), root))
    return answer


def write_to_file():
    f = open("input3.txt")
    array = [s for s in f.readlines()]
    f.close()

    answer = solve(array)

    file2 = open("output3.txt", "w+")
    for el in answer:
        file2.write(str(el) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))

