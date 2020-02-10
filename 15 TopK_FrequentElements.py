input_list = input('Enter list of numbers: ')
input_list = input_list.split(',')
input_list = list(map(int, input_list))

k = int(input('Enter the values of k: '))


def count_frequency(input_list):
    freq_dict = {}
    sort_by_freq = []

    for i in input_list:
        if i in freq_dict.keys():
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    for i in range(len(freq_dict)):
        max_value = max(freq_dict, key=freq_dict.get)
        sort_by_freq.append(max_value)
        del freq_dict[max_value]

    return sort_by_freq


freq = count_frequency(input_list)
freq = freq[:k]
print('Most frequent K elements are: ', freq)


# sorted(freq_dict.values(),reverse=True)