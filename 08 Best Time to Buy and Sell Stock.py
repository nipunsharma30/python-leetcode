
array =[7,1,5,3,6,4]

def buysell(array):
    profit = 0
    buy = 0
    maxProfit = 0
    for i in range(len(array)):
        if i == 0:
            buy = array[i]
            continue
        if array[i] < buy:
            buy = array[i]
        else:
            profit = array[i] - buy
            if profit > maxProfit:
                maxProfit = profit
    print('Max profit is: ', maxProfit)

buysell(array)