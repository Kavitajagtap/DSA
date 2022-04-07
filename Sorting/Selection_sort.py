

def selectionSort(arr):
 for i in range(len(arr)):
    minind = i
    for j in range(i+1,len(arr)):
        if arr[minind] > arr[j]:
            minind = j
    arr[i],arr[minind] = arr[minind],arr[i]
 return arr

print(selectionSort([10,80,110,-110,-1,-67,89,1]))

