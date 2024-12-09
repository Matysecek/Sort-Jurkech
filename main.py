import random


values = list(range(101))
random.shuffle(values)
nahodne_values = values[:10]

print(nahodne_values)

 #BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = (nahodne_values)
sorted_arr = bubble_sort(arr)

print("pole:", sorted_arr)

 #BOGO SORT

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr) 
    return arr
arr = (nahodne_values)
sorted2_arr = bogo_sort(arr)

print("pole:", sorted2_arr)
 
 #SELECTION SORT

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = (nahodne_values)
sorted_arr = selection_sort(arr)

print("pole:", sorted_arr)

 #INSERTION SORT

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = (nahodne_values)
sorted_arr = insertion_sort(arr)

print("pole:", sorted_arr)