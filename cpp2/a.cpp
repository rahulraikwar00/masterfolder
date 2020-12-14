// #include <stdio.h>
// int main() {
//     int k=0, n, i;
//     float arr[100];
//     scanf("%d", &n);
//     scanf("%d", &k);
//     for (i = 0; i < n; ++i) {
//         scanf("%d", &arr[i]);
//     }

//     // storing the largest number to arr[0]
//     for (i = 1; i < k; ++i) {
//         if (arr[0] < arr[i])
//             arr[0] = arr[i];
//     }

//     printf("Largest element = %d", arr[0]);

//     return 0;
// }


#include <stdio.h>

int main() {
	int k=0, n, i;
    float arr[100];
    scanf("%d", &n);
    scanf("%d", &k);
    for (i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }
	
   int loop, largest;

   largest = arr[0];
   
   for(loop = 1; loop < k; loop++) {
      if( largest < arr[loop] ) 
         largest = arr[loop];
   }
   
   printf("Largest element of array is %d", largest);   
   
   return 0;
}


// C program to find maximum in arr[] of size n 
#include <stdio.h> 

// C function to find maximum in arr[] of size n 
int largest(int arr[], int n) 
{ 
	int i, k, n; 
	
	// Initialize maximum element 
	int max = arr[0]; 
	// Traverse array elements from second and 
	// compare every element with current max 
	for (i = 1; i < n; i++) 
		if (arr[i] > max) 
			max = arr[i]; 

	return max; 
} 

int main() 
{ 

    int k=0, n, i;
    float arr[100];
    scanf("%d", &n);
    scanf("%d", &k);
    for (i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }


	int n = sizeof(arr)/sizeof(arr[0]); 
	printf("Largest in given array is %d", largest(arr, n)); 
	return 0; 
} 
