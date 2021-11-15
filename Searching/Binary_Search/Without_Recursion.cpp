#include <iostream>
using namespace std;

int binary_Search(int arr[], int target,int size)
    {
        int start = 0;
        int end = size - 1;
        while(start <= end)
        {
            int mid = start + (end-start)/2;
            if(target < arr[mid])
                end = mid - 1;
            else if(target > arr[mid])
                start = mid + 1;
            else
                return mid;
        }
        return -1;
    }
void input(int arr[], int n)
{
    for(int i = 0; i < n; i++)
        cin>>arr[i];
}
void print(int arr[], int n)
{
    for(int i = 0; i < n; i++)
        cout<<arr[i]<<"\t";
    cout<<"\n";
}

int main()
{
    int arr[20],size,n,x;
    cout <<"How many elements you want..?";
    cin>>size;
    input(arr, size);
    cout<<"which element you want to search..? ";cin>>n;
    x = binary_Search(arr,n,size);
    if(x == -1)
    cout<<"Element not found"<<endl;
    else
    cout<<"Element is found at "<<x+1<<" location"<<endl;
    return 0;
}

/*
-------- Output --------------
How many elements you want..?10
12
34
56
67
71
79
80
85
90
97
which element you want to search..? 79
Element is found at 6 location

*/
