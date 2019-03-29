def even_fibonacci():
    fib_list = [1, 2]
    new_value = 3
    while new_value < 4000000:
        fib_list.append(new_value)
        new_value = fib_list[-1] + fib_list[-2]
    fib_list.append(new_value)
    even_fib_list = []
    for i in range(0, len(fib_list)):
        if i % 2 == 0:
            even_fib_list.append(i)
    sum = 0
    for i in range(0, len(even_fib_list)):
        sum += i
    print(sum)
    return sum


if __name__ == "__main__":
    even_fibonacci()
