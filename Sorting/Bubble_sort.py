'''
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until
 they are not in the intended order.
Just like the movement of air bubbles in the water that rise up to the surface, each element of
 the array move to the end in each iteration. Therefore, it is called a bubble sort.
Time Complexities:  Best    :	O(n)
                    Worst   :	O(n2)
                    Average : 	O(n2)

'''

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubbleSort([10,80,110,-110,-1,-67,89,1]))
