input_num = int(input('Enter any number: '))


def prime(num):
    for i in range(2, num):
        if num == 2:
            print(num, '2 is a prime number')
            return
        if (num % i) == 0:
            print(num, ' is not a prime number')
            return
    print(num, ' is a prime number')


prime(input_num)
