#include <stdio.h>
#include <ctype.h>
#define MAX 50

int compute_word(char word[]);

int main(void){
    char word1[MAX], word2[MAX];
    printf("Player1: ");
    gets(word1);
    printf("Player2: ");
    gets(word2);
    int score1 = compute_word(word1);
    int score2 = compute_word(word2);
    if (score1 > score2){
        printf("Player1 wins.\n");
    }else if (score1 < score2){
        printf("Player2 wins\n");
    }else{
        printf("Draw\n");
    }
    return 0;
}

int compute_word(char word[]){
    //we need to convert lowercase word to uppercase in order to solve this challenge.
    int value_of_letters[27] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int value_of_char_in_ascii[27] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90};
    int value = 0;
    int i = 0; // counter, indentifies the lenght of our word
    while(word[i]){
        i++;
    }
    for(int j=0; j<i; j++){
        for(int k=0; k<26; k++){
            if((int) toupper(word[j]) == value_of_char_in_ascii[k]){
                value += value_of_letters[k];
            }
        }
    }
    printf("%d\n", value);
    return value;
}

