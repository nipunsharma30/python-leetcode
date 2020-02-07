# Calculate moving average: For example:
# Input 10, 20, 30, 10, ...
# Output: 10, 15, 20, 17.5, ...


input_list = input('Enter the list of numbers')
input_list = input_list.split(',')
input_list = list(map(int, input_list))


def moving_avg(input_list):
    moving_avg = []
    moving_sum = 0
    for i in range(len(input_list)):
        moving_sum = moving_sum + input_list[i]
        moving_avg.append(moving_sum/ (i+1))
    print('Moving Average is: ', moving_avg)


moving_avg(input_list)
