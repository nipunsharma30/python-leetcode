#Count the number of prime numbers less than a non-negative number, n.

input_num = int(input('Enter a non negative number: '))


def count_prime(num):
    count = 1
    for i in range(3, num):
        check = 0
        for j in range(2, i):
            if (i % j) == 0:
                check =+ 1
                break
        if check == 0:
            count += 1

    print( 'Number of prime numbers less than a non negative number is: ', count)
    return


count_prime(input_num)
