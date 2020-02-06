input = [1,2,3,4,6]
input = input('Enter the array: ')
input = input.split(',')
input = list(map(int,input))

def stdiv(arr):
    arr_mean = sum(arr)/len(arr)
    print(arr_mean)
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum = arr_sum + (arr[i] - arr_mean)**2
    arr_sum = (arr_sum/len(arr))**1/2
    return arr_sum

result = stdiv(input)
print(result)