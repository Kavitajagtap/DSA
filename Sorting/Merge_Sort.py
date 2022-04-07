
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

test_cases = [
    [78,-90,43,0,45,2,-1000,143],
    [],
    [3],
    [9, 8, 7, 2],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    mergeSort(arr)
    print(arr)

    
    
