import time
import tracemalloc

t_start = time.perf_counter()
tracemalloc.start()


def LargestNumber(digits):
    answer = ""
    while digits:
        maxdigit = digits[0]
        for digit in digits:
            if first_is_better(digit, maxdigit):
                maxdigit = digit
        answer += maxdigit
        digits.remove(maxdigit)
    return answer


def first_is_better(a, b):
    if a[0] > b[0]:
        return True
    if a[0] < b[0]:
        return False
    if len(a) == len(b):
        return a > b
    if len(a) > 1 and len(b) > 1:
        return first_is_better(a[1:], b[1:])
    if len(a) == 1:
        return a > b[1]
    if len(b) == 1:
        return a[1] > b


def solve(digits):
    return LargestNumber(digits)


def write_to_file():
    f = open("input6.txt")
    n = int(f.readline())
    digits = [i for i in f.readline().split()]
    f.close()

    result = solve(digits)
    file2 = open("output6.txt", "w+")
    file2.write(result)


if __name__ == "__main__":
    write_to_file()

    print("Время выполнения: %s секунд " % (time.perf_counter() - t_start))
    print("Затраты памяти: %s КБ " % (tracemalloc.get_traced_memory()[0] / 2 ** 10))
