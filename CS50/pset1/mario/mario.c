#include <stdio.h>

int get_int(void){
    int number;
    do {
        printf("Height: ");
        scanf("%d", &number);
    }while(number < 1 || number > 8);
    return number;
}

int main(void){
    int n = get_int();
    char c = '#';
    for(int i=0; i<n; i++){
        for(int j=0; j<n-i-1; j++){
            printf("%c", ' ');
        }
        for(int k=0; k<=i; k++){
            printf("%c", c);
        }
        printf("%c", ' ');
        for(int l=0; l<=i; l++){
            printf("%c", c);
        }
        printf("\n");
    }
    return 0;
}