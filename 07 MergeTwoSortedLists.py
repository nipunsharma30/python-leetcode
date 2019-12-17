inputlist1 = input('Enter list 1: ')
inputlist1 = inputlist1.split(',')
inputlist1 = list(map(int,inputlist1))
inputlist2 = input('Enter list 2: ')
inputlist2 = inputlist2.split(',')
inputlist2 = list(map(int, inputlist2))

def combinedlist(inputlist1, inputlist2):
    x,y = 0,0
    combined = []
    for i in range(len(inputlist1) + len(inputlist2)):
        if inputlist1[x] <= inputlist2[y]:
            combined.append(inputlist1[x])
            x += 1
            if x == len(inputlist1):
                combined.extend(inputlist2[y:])
                return combined
        else:
            combined.append(inputlist2[y])
            y += 1
            if y == len(inputlist2):
                combined.extend(inputlist1[x:])
                return combined

combined = combinedlist(inputlist1,inputlist2)

print(combined)

