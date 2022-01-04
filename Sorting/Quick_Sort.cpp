
#include <iostream>
using namespace std;

void get_input(int arr[20], int n);
void display(int arr[20], int n);
void quick_sort(int arr[20], int low, int high);

int main()
{
    int arr[20],num,n,low = 0;
    char ch;
    do
    {
        cout<<"\nEnter your choice: \n 1. Give input: \n 2. Display Elements: \n 3. Sort elements: "<<endl;
        cin>>num;
        switch(num)
        {
        case 1 : cout<<"Enter how many elements you want to sort: ";cin>>n;
                 get_input(arr, n);
                 break;
        case 2 : cout<<"Array elements are: "<<endl;
                 display(arr, n);
                 break;
        case 3 : quick_sort(arr, low, n-1);
                 cout<<"Soring is done!!"<<endl;
                 break;
        }
        cout<<"\nDo you want to continue?(Y/N) ";
        cin>>ch;
    }
    while(ch == 'Y' || ch == 'y');
     return 0;
}
void get_input(int arr[], int n)
{
    cout<<"Enter "<<n<<" elements: "<<endl;
    for(int i = 0; i < n; i++)
        cin>>arr[i];
}

void display(int arr[], int n)
{
    for(int i = 0; i < n; i++)
        cout<<arr[i]<<"\t";
    cout<<"\n";
}

void quick_sort(int arr[], int low, int high)
{
    int i = low, j = high;
    int pivot = arr[low];
    if(low < high)
    {
        while(i < j)
        {
            while(arr[i] <= pivot)
                i++;
            while(arr[j] > pivot)
                j--;
            if(i < j)
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    int temp = arr[low];
    arr[low] = arr[j];
    arr[j] = temp;
    quick_sort(arr,low,high-1);
    quick_sort(arr,low+1,high);
}
}
/*
---------------- Output --------------------------

Enter your choice:
 1. Give input:
 2. Display Elements:
 3. Sort elements:
1
Enter how many elements you want to sort: 10
Enter 10 elements:
89 34 0 77 45 63 90 28 2 51

Do you want to continue?(Y/N) Y

Enter your choice:
 1. Give input:
 2. Display Elements:
 3. Sort elements:
2
Array elements are:
89      34      0       77      45      63      90      28      2       51

Do you want to continue?(Y/N) Y

Enter your choice:
 1. Give input:
 2. Display Elements:
 3. Sort elements:
3
Soring is done!!

Do you want to continue?(Y/N) Y

Enter your choice:
 1. Give input:
 2. Display Elements:
 3. Sort elements:
2
Array elements are:
0       2       28      34      45      51      63      77      89      90

Do you want to continue?(Y/N) N
*/
