
array =[7,1,5,3,6,4]


def profit(array):
    buy = 0
    sell = 0
    profit = [0]
    for i in range(len(array)):
        buy = array[i]
        for j in range(i+1,len(array)):
            sell = array[j]
            profit.append((sell - buy))
    print('max profit is: ', max(profit))

profit(array)

