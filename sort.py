#sorting in python
#https://github.com/turbocornball/CSC-124.git 

#timing two different sorting algorithms in python with a random list 
#of integers, each function is given the same list (fresh copy each time)

import random #for generating random numbers
import time   #for timing each sort function

N = 10      #number to be multiplied in every iteration of the list
list = []   #list of integers

#loop for generating 100, 1000, 10000, up to 100000 integers
while N <= 100000:
    N*=10
    for i in range(0, N):
        list.append(random.randint(0, N))

    #insertion sort
    def insertionSort(list):
        past=time.time()
        for index in range(1,len(list)):
            currentvalue = list[index]
            position = index

            while position > 0 and list[position-1] > currentvalue:
                list[position] = list[position-1]
                position = position
            
            list[position] = currentvalue
        print("Insertion Sort Execution Time: {} seconds".format(time.time()-past))

    #merge sort
    def mergeSort(list):
        if len(list)>1:
            mid = len(list)//2
            lefthalf = list[:mid]
            righthalf = list[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)
            i=j=k=0       
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    list[k]=lefthalf[i]
                    i=i+1
                else:
                    list[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                list[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                list[k]=righthalf[j]
                j=j+1
                k=k+1
        
    past = time.time()
    mergeSort(list)
    print("Merge Sort Execution Time: {} seconds" .format(time.time()-past))
    insertionSort(list)

"""
typical results: for 100, 1000, 10000, 100000 integer input respectively
Merge Sort Execution Time: 0.1569 seconds
Insertion Sort Execution Time: 0.0 seconds
Merge Sort Execution Time: 0.0330 seconds
Insertion Sort Execution Time: 0.00105 seconds
Merge Sort Execution Time: 0.3775 seconds
Insertion Sort Execution Time: 0.0 seconds
Merge Sort Execution Time: 4.850 seconds
Insertion Sort Execution Time: 0.156 seconds
Merge Sort Execution Time: 59.482 seconds
Insertion Sort Execution Time: 1.697 seconds
"""
