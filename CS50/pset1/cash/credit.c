#include <stdlib.h>
#include <stdio.h>
#include <math.h>

long get_long(void){
    long int num;
    do
    {
        printf("enter a credit card number: ");
        scanf("%ld", &num);
    } while (num < 1 || num > 9999999999999999);
    return num;
}


int main(){
    long int number = get_long();
    int nDigits = floor(log10(labs(number))) + 1;
    printf("digit %d", nDigits);
    int ctr = 0;
    int sum = 0;
    for(int i=0; i<nDigits; i++){
        //check for odd or even
        ctr += 1;
        
        if(ctr % 2 == 0){
            int temp = number % 10;
            temp *= 2;
            if(temp >= 10){
                temp = temp % 10 + 1;
                sum += temp;
            }else{
                sum += temp;
            }
        }else{
            sum += number % 10;
        }
    }
    printf("%d", sum);
    return 0;
}