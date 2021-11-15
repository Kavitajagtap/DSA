
#include <iostream>
using namespace std;

int binary_Search(int arr[], int l, int h, int target)
{
    if (l <= h)
    {
        int mid = l + (h - l) / 2;
        if (arr[mid] == target)
            return mid;
        if (target< arr[mid])
            return binarySearch(arr, l, mid - 1, target);
        return binarySearch(arr, mid + 1, h, target);
    }
    return -1;
}
void input(int arr[], int n)
{
    for(int i = 0; i < n; i++)
        cin>>arr[i];
}
int main()
{
    int arr[20],size,n,x,low = 0;
    cout <<"How many elements you want? ";cin>>size;
    input(arr, size);
    cout<<"which element you want to search..? ";cin>>n;
    x = binary_Search(arr,low,size-1,n);
    if(x == -1)
    cout<<"Element not found"<<endl;
    else
    cout<<"Element is found at "<<x+1<<" location"<<endl;
    return 0;
}
/*
----------- Output ------------

How many elements you want? 7
10
23
45
67
89
123
140
which element you want to search..? 123
Element is found at 6 location

*/
