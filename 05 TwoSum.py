#Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def two_sum(given_nums,target):
    output = []
    skip = []
    my_dict = {x: 1 for x in given_nums}
    for i in my_dict.keys():
        if i not in skip:
            if (target - i) in my_dict:
                output.append([i, (target - i)])
                skip.append((target-i))
    return output

target = int(input('Enter the target number: '))
given_nums = input('Enter numbers for the two sum problem: ')
given_nums = given_nums.split(',')
given_nums = list(map(int, given_nums))

result = two_sum(given_nums,target)
if len(result)>0:
    print(result)
else:
    print('No Match Found')