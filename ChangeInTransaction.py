trans = int(input('Enter the transaction amount: '))
cash =  int(input('Enter the cash given by the customer'))

change_avail = {50: 0,
                20: 0,
                10: 0,
                5: 0,
                1: 0,
                0.5: 0,
                0.25: 0,
                0.1: 0,
                0.05: 0,
                0.01: 0}

change = (cash - trans)
print(change)
for i in change_avail.keys():
    if change >= i:
        change_avail[i] = int(change / i)
        print(change % i)
        change = change - (i*change_avail[i])


print('change: ', change_avail)



