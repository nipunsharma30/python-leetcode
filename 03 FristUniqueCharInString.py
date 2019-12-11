string = input('Enter a string: ')

def dist_char(string):
    dic = {}
    for i in string:
        if i in dic.keys():
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1
    for i in string:
        if dic[i]==1:
            first_char = i
            break
    return first_char


print('the first unique character is ', dist_char(string))