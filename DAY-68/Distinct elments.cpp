// Program to print all distinct elements of given input arrays. Also print the total of the distinct elements.

#include <bits/stdc++.h> 
using namespace std; 
  
void printUncommon(int arr1[], int arr2[],  
                           int n1, int n2) 
{ 
  
    int i = 0, j = 0, k = 0,c=0; 
    while (i < n1 && j < n2) { 
  
        // If not common, print smaller 
        if (arr1[i] < arr2[j]) { 
            cout << arr1[i] << " "; 
            i++; 
            k++; 
            c+=1;
        } 
        else if (arr2[j] < arr1[i]) { 
            cout << arr2[j] << " "; 
            k++; 
            j++; 
            c+=1;
        } 
  
        // Skip common element 
        else { 
            i++; 
            j++; 
        } 
    } 
  
    // printing remaining elements 
    while (i < n1) { 
        cout << arr1[i] << " "; 
        i++; 
        k++;
        c+=1;
    } 
    while (j < n2) { 
        cout << arr2[j] << " "; 
        j++; 
        k++;
        c+=1;
    } 
    cout<<"\n"<<c;
} 
  
// Driver code 
int main() 
{ 
    int arr1[] = {1,2,3,4,5}; 
    int arr2[] = {2,6,8,10}; 
  
    int n1 = sizeof(arr1) / sizeof(arr1[0]); 
    int n2 = sizeof(arr2) / sizeof(arr2[0]); 
  
    printUncommon(arr1, arr2, n1, n2); 
  
    return 0; 
} 
