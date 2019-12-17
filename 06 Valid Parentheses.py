# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

input_string = input('Enter a string :')

valid_dict = dict((['(',')'],['[',']'],['{','}']))
# i=0
def valid_parentheses(input_string, valid_dict):
    stack = []
    for i in range(len(input_string)):
        #to check if the string contains other characters than valid_string
        if input_string[i] not in (valid_dict.keys() | valid_dict.values()):
            return 'Invalid String'

        if len(stack) == 0:
            if input_string[i] not in valid_dict.keys():
                return 'Invalid String'
            stack.append(input_string[i])
        else:
            if valid_dict[stack[-1]] == input_string[i]:
                stack.pop()
            else:
                stack.append(input_string[i])

    if (len(stack) == 0):
        return 'Valid String'
    else:
        return 'Invalid String'
if len(input_string) == 0:
    print('Valid String')
else:
    result = valid_parentheses(input_string, valid_dict)
    print(result)



