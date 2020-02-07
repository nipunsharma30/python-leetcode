# Check if string is palindrome or not
input_str = input('Enter a string: ')

def is_palindrome(str):
    n = int(len(str)/2)
    for i in range(n):
        if (str[-i-1]) == (str[i]):
            continue
        else:
            print('The string is not a palindrome')
            return
    print('String is palindrome')


is_palindrome(input_str)
