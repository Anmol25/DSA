#include <iostream>
using namespace std;

void BubbleSort(int arr[], int n){
    for(int count = 0; count <=n-1; count++){
        for(int j = 0;j<=n-2;j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j],arr[j+1]);
            }
        }
    }
}


int main(){
    int arr[] = {1000, 4, 90, 80, 20, 40, -2};
    for(int i = 0; i<7;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    BubbleSort(arr, 7);

    for(int i = 0; i<7;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}