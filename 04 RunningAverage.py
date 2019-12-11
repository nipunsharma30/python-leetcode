def cal_running_avg(user_input):
    avg = []
    input_sum = 0
    for i in range(len(user_input)):
        input_sum = input_sum + user_input[i]
        #     print(i)
        avg.append(input_sum / (i + 1))
    return avg

user_input = input('Enter numbers for running total: ')
user_input = user_input.split(',')
user_input = list(map(int, user_input))
running_average = cal_running_avg(user_input)
print('Running average is for the input is: ', running_average)