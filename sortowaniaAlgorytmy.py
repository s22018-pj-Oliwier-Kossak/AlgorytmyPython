import numpy as np
import time
import sys
sys.setrecursionlimit(10**6)
print(sys.getrecursionlimit())
def CreateArraySortfromBiggerToSmaller():
    deck2 = []
    for i in (range(300000, 0, -1)):
        deck2.append(i)
    f = open('output3.txt', 'w')
    f.write('{}'.format(deck2))
    f.close()
    return deck2
def ReadArraySortfromBiggerToSmaller():
    text_file = open("output3.txt", "r")
    text_file.close()
    return CreateArraySortfromBiggerToSmaller()

def CreateArraySortfromSamllerToBigger():
    deck = list(range(1, 300000))
    f = open('output2.txt', 'w')
    f.write('{}'.format(deck))
    f.close()
    return deck
def ReadArraySortfromSamllerToBigger():
    text_file = open("output2.txt", "r")

    text_file.close()
    return CreateArraySortfromSamllerToBigger()

def CreateArrayRandom():
    arr = np.random.randint(1, 100, 300000)
    f = open('output1.txt', 'w')
    f.write('{}'.format(arr))
    f.close()
    return arr
def ReadArrayRandom():
    text_file = open("output1.txt", "r")
    print(CreateArrayRandom())
    text_file.close()
    return CreateArrayRandom()

def MaxHeapif(A,n,i):
    left=2*i+1
    right=2*i+2
    if (left<n and A[i]<A[left]):
        largest = left
    else:
        largest=i
    if (right < n and A[largest]<A[right]):
        largest=right
    if (largest !=i):
        A[largest],A[i]=A[i],A[largest]
        MaxHeapif(A,n,largest)




def HEapSort(A):
    n=len(A)
    for i in range(n // 2, -1, -1):
        MaxHeapif(A,n, i)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        MaxHeapif(A, i,0)

def QuickSort(A,p,r):

    if p<r:
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r,1):
        if A[j]<=x:
            i=i+1
            A[j],A[i]=A[i],A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def InsertionSort(A):
    for j in range(len(A)):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

def MerrgeSort(arr):
    if len(arr)>1:

        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        MerrgeSort(left)
        MerrgeSort(right)

        i=0
        j=0
        k=0
        while i< len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k]= right[j]
                j+=1
            k+=1

        while i< len(left):
            arr[k]=left[i]
            i+=1
            k+= 1
        while j< len(right):
            arr[k]=right[j]
            j+= 1
            k+= 1

def countingSort(arr):
    n = len(arr)
    arr1 = [0] * n

    x = [0] * 300001

    for i in range(0, n):
        x[arr[i]] += 1

    for i in range(1, 300001):
        x[i] += x[i - 1]


    i = n - 1
    while i >= 0:
        arr1[x[arr[i]] - 1] = arr[i]
        x[arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = arr1[i]

x=CreateArrayRandom()
x2=CreateArraySortfromSamllerToBigger()
x3=CreateArraySortfromBiggerToSmaller()
y1=ReadArrayRandom()
y2=ReadArraySortfromSamllerToBigger()
y3=ReadArraySortfromBiggerToSmaller()

start_time = time.time()
HEapSort(y1)
print(" HeapSort NiePosortowana tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
HEapSort(y2)
print(" HeapSort Posortowana od najmniejszej do najwiekszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
HEapSort(y3)
print(" HeapSort  Posortowana od  najwiekszej do najmniejszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
MerrgeSort(y1)
print(" MerrgeSort NiePosortowana tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
MerrgeSort(y2)
print(" MerrgeSort Posortowana od najmniejszej do najwiekszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
MerrgeSort(y3)
print(" MerrgeSort Posortowana od  najwiekszej do najmniejszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
countingSort(y1)
print(" countingSort NiePosortowana tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
countingSort(y2)
print(" countingSort Posortowana od najmniejszej do najwiekszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
countingSort(y3)
print(" countingSort  Posortowana od  najwiekszej do najmniejszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
QuickSort(y1,0,299999)
print(" QuickSort NiePosortowana tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
QuickSort(y2,0,299999)
print(" QuickSort Posortowana od najmniejszej do najwiekszej tablica czas: --- %s seconds ---" % (time.time() - start_time))
start_time=0

start_time = time.time()
QuickSort(y3,0,299999)
print(" QuickSort  Posortowana od  najwiekszej do najmniejszej tablica czas: --- %s seconds ---" % (time.time() - start_time))