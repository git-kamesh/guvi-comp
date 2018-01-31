#include<stdio.h>
/**
* Author : KAMESH S <1234.kamesh@gmail.com>
*
* Ouput :
*    Enter two numbers:
*    5
*    10
*
*    Sum : 15
*/

// Function to add
int add(int a,int b){
    return a+b;
}
int main(){
    int a,b;

    // Get The input
    printf("Enter two numbers:\n");
    scanf("%d\n%d",&a,&b);

    // Solve and print
    printf("\nSum : %d\n",add(a,b));
}
