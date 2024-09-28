import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1


Root = None


def get_size(root):
    if root is None:
        return 0
    return root.size


def insert(from_root, key):
    global Root

    if Root is None:
        Root = Node(key)
        return Root

    if key < from_root.key:
        if from_root.left is None:
            from_root.left = Node(key)
        else:
            from_root.left = insert(from_root.left, key)

    elif key > from_root.key:
        if from_root.right is None:
            from_root.right = Node(key)
        else:
            from_root.right = insert(from_root.right, key)

    from_root.size = 1 + get_size(from_root.left) + get_size(from_root.right)
    return from_root


def tree_min(x):
    while x.left is not None:
        x = x.left
    return x


def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        temp = tree_min(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    root.size = 1 + get_size(root.left) + get_size(root.right)
    return root


def find_k_max(root, k):
    if root is None:
        return None
    right_size = get_size(root.right)
    if right_size + 1 == k:
        return root.key
    elif k <= right_size:
        return find_k_max(root.right, k)
    else:
        return find_k_max(root.left, k - right_size - 1)


def solve(commands):
    global Root
    answers = []
    commands = [line.split() for line in commands]
    for command in commands:
        if command[0] == "+1":
            insert(Root, int(command[1]))
        elif command[0] == "0":
            result = find_k_max(Root, int(command[1]))
            if result:
                answers.append(result)
        elif command[0] == "-1":
            Root = delete_node(Root, int(command[1]))
    return answers


def write_to_file():
    f = open("input16.txt")
    n = int(f.readline())
    commands = [f.readline().strip() for _ in range(n)]
    f.close()

    answers = solve(commands)
    file2 = open("output16.txt", "w+")
    for i in range(len(answers)):
        file2.write(str(answers[i]) + "\n")
    file2.close()


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
