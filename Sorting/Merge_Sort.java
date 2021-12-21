package com.sort;
import java.util.*;

public class MergeSort{
    public static void main(String[] args) {
        int[] arr = {11,30,24,7,31,16,39,41};
        System.out.println("Array before sorting: ");
        System.out.println(Arrays.toString(arr));
        mergeSort(arr,0,arr.length-1);
        System.out.println("Array after sorting: ");
        System.out.println(Arrays.toString(arr));
    }
    static void mergeSort(int[] arr,int lb,int ub) {
        if (lb < ub) {
            int mid = (lb + ub) / 2;
            mergeSort(arr, lb, mid);
            mergeSort(arr, mid + 1, ub);
            merge(arr, lb, mid, ub);
        }
    }
    static void merge(int[] arr, int lb, int mid, int ub)
    {
        int i = lb, j = mid+1,k = lb;
        int[] b = new int[arr.length];

        while(i <= mid && j <= ub) {
            if(arr[i] <= arr[j]) {
                b[k] = arr[i];
                i++;
            }
            else {
                b[k] = arr[j];
                j++;
            }
            k++;
        }
        if(i > mid){
            while(j <= ub){
                b[k] = arr[j];
                k++;j++;
            }
        }
        else{
            while(i <= mid){
                b[k] = arr[i];
                k++;i++;
            }
        }
        for(k = lb; k <= ub; k++)
            arr[k] = b[k];
    }
}
/*
----------------- Output --------------------

Array before sorting: 
[11, 30, 24, 7, 31, 16, 39, 41]
Array after sorting: 
[7, 11, 16, 24, 30, 31, 39, 41]

*/
