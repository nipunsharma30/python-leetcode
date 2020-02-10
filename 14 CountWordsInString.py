# Given a string, count number of words in it. The words are separated by following characters: space (‘ ‘) or new line (‘\n’) or tab (‘\t’) or a combination of these.


input_str = input('Enter a string: ')
special_char = [' ', '\n', '\t']


def count_words(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i] not in special_char:
            count += 1
    print('Number of words in string are: ', count)


count_words(input_str)
