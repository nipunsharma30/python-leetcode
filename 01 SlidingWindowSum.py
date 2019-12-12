
def slidingsum(user_input):
    x = sum(user_input[:k])
    b = []
    for i in range(len(user_input)-k +1):
        if i==0:
            b.append(x)
        else:
            x = x - user_input[i-1] + user_input[i+2]
            b.append(x)
    return b

k = int(input('Enter sliding size: '))
user_input = input('Enter numbers for running total: ')
user_input = user_input.split(',')
user_input = list(map(int, user_input))

final_output = slidingsum(user_input)
print(final_output)