#include <iostream>
using namespace std;

int search(int arr[], int size, int key)
{
    for(int i = 0; i < size; i++)
    {
        if(arr[i] == key)
            return i;
    }
    return -1;
}

int main()
{
   int size;
   cout<<"Enter how many element you want? ";
   cin>>size;
   int arr[size],key;
   for(int i = 0; i < size; i++)
   {
       cin>>arr[i];
   }
   cout<<"Enter which element you want to search? ";
   cin>>key;
   int result = search(arr, size, key);
   if(result == -1)
      cout<<"element is not present in the array."<<endl;
   else
      cout<<"element is present in the array at "<<result+1<<" position."<<endl;

    return 0;
}

/*

Enter how many element you want? 5
10
34
56
78
90
Enter which element you want to search? 56
element is present in the array at 3 position.

*/
