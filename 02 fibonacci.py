def fibonacci(n):
    list = []
    for i in range(n):
        if i <= 1:
            list.append(i)
        else:
            x = (list[i - 1] + list[i - 2])
            list.append(x)
    return list

num_of_elements = int(input('Enter the number of elements: '))
fibonacci_series = fibonacci(num_of_elements)
print(fibonacci_series)