from collections import Counter
import numpy as np



file = open("C:\\Users\PC\\Desktop\\desktop.txt", "r")
data = file.read()

counter = Counter(data)

a = []
b = []


for x in counter.values():
    print("values: ", x)
    a.append(x)

for y in counter.keys():
    print("keyes: ", y)
    b.append(y)

print("a: ", a)
print()
print("b:", b)
print()
c = np.vstack((a, b)).T
print("c: ", c)

print()
print()


def MinHeapif(A, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and A[i] > A[left]):
        smallest = left
    else:
        smallest = i
    if (right < n and A[smallest] > A[right]):
        smallest = right
    if (smallest != i):
        A[smallest], A[i] = A[i], A[smallest]
        b[smallest], b[i] = b[i], b[smallest]
        MinHeapif(A, n, smallest)


def buildHeap(A):
    n = len(A)
    for i in range(n // 2, -1, -1):
        MinHeapif(A, n, i)


def scalenie(arr, arr2):
    i = 0
    i = i + 1

    for i in range(1, len(arr)):

        print("obrót :", i)
        buildHeap(arr)
        print("heap a: ", arr)
        print("heap b: ", arr2)
        if len(arr) > 2:

            first = arr[0]
            second = arr[1]
            third = arr[2]

            first2 = arr2[0]
            second2 = arr2[1]
            third2 = arr2[2]

            if (arr[1] > arr[2]):

                n = first + third
                n2 = first2 + third2
                arr.remove(first)
                arr.remove(third)
                arr2.remove(first2)
                arr2.remove(third2)
            else:
                n = first + second
                arr.remove(first)
                arr.remove(second)

                n2 = first2 + second2
                arr2.remove(first2)
                arr2.remove(second2)

            # print("first: ", first)
            # print("second: ", second)
            # print("third: ", third)
            # print("n ", n)
            # print()
            # print("first2: ", first2)
            # print("second2: ", second2)
            # print("third2: ", third2)
            # print("n ", n2)

            arr.append(n)
            arr2.append(n2)
            print("append a: ", arr)
            print("append b: ", arr2)
            buildHeap(arr)
            print("heap a: ", arr)
            print("heap b: ", arr2)

            print()
            print("#########")
            print()
        else:

            first = arr[0]
            second = arr[1]

            first2 = arr2[0]
            second2 = arr2[1]

            n = first + second

            n2 = first2 + second2

            # print("first: ", first)
            # print("second: ", second)
            # print("n ", n)
            #
            # print("first2: ", first2)
            # print("second2: ", second2)
            # print("n2 ", n2)

            arr.remove(first)
            arr.remove(second)
            arr.append(n)

            arr2.remove(first2)
            arr2.remove(second2)
            arr2.append(n2)

            print("append a: ", arr)
            print("append b: ", arr2)

            buildHeap(arr)

            print()
            print("#########")
            print()


scalenie(a, b)
print(a)
print(b)
