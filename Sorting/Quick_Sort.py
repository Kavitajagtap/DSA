

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        l = [i for i in arr if i < pivot]
        h = [i for i in arr if i > pivot]
        return quickSort(l) + [pivot] + quickSort(h)

print(quickSort([78,-90,43,0,45,2,-1000,143]))

