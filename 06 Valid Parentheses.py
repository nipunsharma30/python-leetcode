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

result = valid_parentheses(input_string, valid_dict)
print(result)



