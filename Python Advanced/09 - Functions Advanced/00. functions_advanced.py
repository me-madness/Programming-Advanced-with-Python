def sum_nums(a, b , *args):
    total_sum = a + b
    for el in args:
        total_sum += el
    return total_sum


print(sum_nums( a = 5, b = 7, *args: 3, 7, 10, 15))