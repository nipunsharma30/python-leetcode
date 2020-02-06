
num = int(input('Enter any number: '))
divisor = 0
def prime(num):

    for i in range(2, num):
        if i != 2:
            if (num % i) == 0:
                divisor = i
                print(divisor)
                return divisor
        else:
            if (num % i) == 0:
                divisor = i
                print(divisor)
                return divisor

divisor = prime(num)

if divisor is None:
    print(num, ' is a prime number')
else:
    print(num, ' is divisable by ', divisor)