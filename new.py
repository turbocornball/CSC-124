import random

N = 100
list = []

for i in range(0, N):
    list.append(random.randint(0, N-1))

def insertionSort(list):
    for index in range(1,len(list)):
        currentvalue = list[index]
        position = index

        while position > 0 and list[position-1] > currentvalue:
            list[position] = list[position-1]
            position = position-1
        
        list[position] = currentvalue

insertionSort(list)
print(list)

#print(list)


