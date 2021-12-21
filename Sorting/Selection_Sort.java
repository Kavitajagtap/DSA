package com.sort;
import java.util.*;

public class SelectionSort{ 
    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);
        int n;
        System.out.println("enter how many elements you want? ");
        n = ip.nextInt();
        System.out.println("Enter " + n + " elements to sort..");
        int[] arr = new int[n];
        input(arr);
        selectionSort(arr);
        System.out.print( "sorted array: "+ Arrays.toString(arr));
    }
    static void input(int[] arr)
    {
        Scanner ip = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++)
            arr[i] = ip. nextInt();
    }
    static void selectionSort(int[] arr)
    {
        for(int i = 0; i < arr.length; i++) {
            int last = arr.length - i - 1;
            int maxIndex = maxIndex(arr, 0, last);
            swap(arr, maxIndex, last);
        }
    }
    static void swap(int[] arr, int maxIndex, int last)
    {
        int temp = arr[maxIndex];
        arr[maxIndex] = arr[last];
        arr[last] = temp;
    }
    static int maxIndex(int[] arr, int start, int end)
    {
        int max = start;
        for(int i = start; i <= end; i++)
        {
            if(arr[max] < arr[i]){
                max = i;
            }
        }
        return max;
    }
}

/*
-----------------Output--------------------------
     
Enter how many elements you want? 
9
Enter 9 elements to sort..
-80 -32 10 0 9 21 -78 -1 5
sorted array: [-80, -78, -32, -1, 0, 5, 9, 10, 21]

*/
