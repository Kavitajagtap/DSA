#include <iostream>
using namespace std;

void merge(int a[], int lb, int mid, int ub)
{
    int i,j,k;
    i = lb;
    j = mid+1;
    k = lb;
    int b[lb+ub];
    while(i <= mid && j <= ub)
    {
        if(a[i] <= a[j]){
            b[k] = a[i];
            i++;
        }
        else{
            b[k] = a[j];
            j++;
        }
        k++;
    }
    if(i > mid){
        while(j <= ub){
            b[k] = a[j];
            j++;
            k++;
        }
    }
    else{
        while(i <= mid){
            b[k]=a[i];
            i++;
            k++;
        }
    }
    for(int k = lb; k <= ub; k++){
        a[k] = b[k];
    }
}
void printArray(int a[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout<<a[i]<<" ";
}
void mergeSort(int a[],int lb,int ub)
{
    if(lb < ub)
    {
        int mid = (lb+ub)/2;
        mergeSort(a,lb,mid);
        mergeSort(a,mid+1,ub);
        merge(a,lb,mid,ub);
    }
}
int main()
{
    int a[] = { 11, 30, 24, 7, 31, 16, 39, 41 };
    int n = sizeof(a) / sizeof(a[0]);
    cout<<"Before sorting array elements are - \n";
    printArray(a, n);
    mergeSort(a, 0, n - 1);
    cout<<"\nAfter sorting array elements are - \n";
    printArray(a, n);
    return 0;

    return 0;
}
/*
----------------- Output --------------------
Before sorting array elements are -
11 30 24 7 31 16 39 41
After sorting array elements are -
7 11 16 24 30 31 39 41
*/
