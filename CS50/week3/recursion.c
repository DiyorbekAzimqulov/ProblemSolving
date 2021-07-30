#include <stdio.h>

int collatz(int n, int steps){
    steps += 1;
    if (n == 1){
        return steps-1;
    }else if(n % 2 == 0){
        return collatz((int) n/2, steps);
    }else {
        return collatz(3*n + 1, steps);
    }
}

int main(void){
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    int steps = collatz(number, 0);
    printf("%d\n", steps);
    return 0;
}