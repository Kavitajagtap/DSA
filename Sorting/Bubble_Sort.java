package com.sort;
import java.util.*;

public class BubbleSort{
    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);
        int n;
        System.out.println("enter how many elements you want? ");
        n = ip.nextInt();
        System.out.println("Enter " + n + " elements to sort..");
        int[] arr = new int[n];
        input(arr);
        bubbleSort(arr);
        System.out.print( "sorted array: "+ Arrays.toString(arr));
    }
  
    static void input(int[] arr)
    {
        Scanner ip = new Scanner(System.in);
        for(int i = 0; i < arr.length; i++)
            arr[i] = ip. nextInt();
    }
  
    static void bubbleSort(int[] arr)
    {
        int i;
        boolean swapped = true;
        for(i = 0; i < arr.length; i++)
        {
            swapped = false;
            for(int j = 1; j < arr.length-i; j++)
            {
                if(arr[j] < arr[j-1])
                {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j-1] = temp;
                    swapped = true;
                }
            }
            if(!swapped)
                System.out.println("Array is already in sorted condition");
                break;
        }
    }
}
/*

enter how many elements you want? 
7
Enter 7 elements to sort..
-7 -80 -2 20 0 1 888
sorted array: [-80, -7, -2, 0, 1, 20, 888]

*/
