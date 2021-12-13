
package com.sort;
import java.util.*;

public class InsertionSort{
    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);
        int n;
        System.out.println("enter how many elements you want? ");
        n = ip.nextInt();
        System.out.println("Enter " + n + " elements to sort..");
        int[] arr = new int[n];
        input(arr);
        insertionSort(arr);
        System.out.print( "sorted array: "+ Arrays.toString(arr));
    }
    
    static void input(int[] arr)
    {
        Scanner ip = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++)
            arr[i] = ip. nextInt();
    }
    
    static void insertionSort(int[] arr)
    {
        for(int i = 0; i < arr.length - 1; i++)
        {
            for(int j = i + 1; j > 0; j--)
            {
                if(arr[j] < arr[j - 1])
                    swap(arr, j, j-1);
                else
                    break;
            }
        }
    }
    
    static void swap(int[] arr, int maxIndex, int last)
    {
        int temp = arr[maxIndex];
        arr[maxIndex] = arr[last];
        arr[last] = temp;
    }
}
/*

enter how many elements you want? 
9
Enter 9 elements to sort..
-4 -89 5 0 43 -1 1 2 3
sorted array: [-89, -4, -1, 0, 1, 2, 3, 5, 43]

*/
