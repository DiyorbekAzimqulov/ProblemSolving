#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){
    char *s = "Assalomu alaykum";
    char *c = malloc(strlen(s)+1);
    for (int i=0; i<=strlen(s); i++ ){
        c[i] = s[i];
    }
    printf("%s\n", c);
    return 0;
}