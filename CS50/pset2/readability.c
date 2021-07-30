#include <stdio.h>
#include <ctype.h>
#include <math.h>
#define MAX 1000

int count_letters(char text[]);
int count_words(char text[]);
int count_sentences(char text[]);


int main(void){
    char text[MAX];
    printf("Text: ");
    gets(text);
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    double index = (0.0588 * letters)/(float) words * 100 - (0.296 * sentences)/(float) words * 100 - 15.8;
    if (round(index) < 1){
        printf("Before Grade 1\n");
    }else if(round(index) > 16){
        printf("Grade 16+\n");
    }else{
        printf("Grade %d\n",(int) round(index));
    }
    return 0;
}

int count_letters(char text[]){
    // isalpha identifies wheter it is alphabetic
    int i = 0;
    int letters = 0;
    while(text[i]){
        if(isalpha(text[i])){
            letters += 1;
        }
        i++;
    }
    return letters;
}

int count_words(char text[]){
    // isspace identifies wheter it is white-space
    int i=0;
    int words = 0;
    while(text[i]){
        if(isspace(text[i])){
            words += 1;
        }
        i++;
    }
    return words;
}

int count_sentences(char text[]){
    // isspace identifies wheter it is white-space
    int i=0;
    int sentences = 0;
    while(text[i]){
        if((int) text[i] == 46 || (int) text[i] == 63 || (int) text[i] == 33){
            sentences += 1;
        }
        i++;
    }
    return sentences;
}