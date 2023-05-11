#include <stdio.h>

int main(){
    int arr[] = {2,4,6,8,10};
    int x = 8;

    int arrLen = sizeof(arr)/ sizeof(arr[0]);
    int isElementPresent = 0;

    for (int i = 0; i < arrLen; i++) {
        if (arr[i] == x) {
            isElementPresent = 1;
            break;
        }
    }

    if (isElementPresent){
        printf("%d is element present in this array\n", x);
    } else {
        printf("%d is not present in this array\n", x);
    }


    return 0;
}