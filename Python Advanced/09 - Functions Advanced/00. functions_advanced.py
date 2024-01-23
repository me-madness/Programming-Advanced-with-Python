def sum_nums(*args):
    total_sum = 0
    for el in args:
        total_sum += el
    return total_sum


print(sum_nums(*args: 3, 7, 10, 15))