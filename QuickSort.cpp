#include <iostream>
using namespace std;

int partition(int arr[], int s, int e){
    int i = s;
    int pivot = arr[e];
    for(int j = s; j<e; j++){
        if (arr[j] < pivot){
            swap(arr[i],arr[j]);
            i++;
        }
    }
    swap(arr[i],arr[e]);
    return i;
}


void QuickSort(int arr[], int s, int e){
    if (s>=e){
        return;
    }
    int p = partition(arr,s,e);
    QuickSort(arr,s,p-1);
    QuickSort(arr,p+1,e);
}

int main(){
    int arr[] = {1000, 4, 90, 80, 20, 40, -2};
    for(int i = 0; i<7;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    QuickSort(arr,0, 7);

    for(int i = 0; i<7;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}