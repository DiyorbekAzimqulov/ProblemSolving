#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

typedef struct{
    char name[MAX];
    int votes;
}candidate;

candidate candidates[10];

int main(int argc, char *argv[]){
    if (argc < 2){
        printf("Usage: ./plurality <name> or multiple names with space separated.");
        return 1;
    }
    int voters = 0;
    for(int i=1; i<argc; i++){
        strcpy(candidates[i-1].name, argv[i]);
        candidates[i].votes = 0;
    }
    printf("Enter number of voters: ");
    scanf("%d", &voters);
    for(int j=0; j<voters; j++){
        char candidate[MAX];
        printf("Vote: ");
        scanf("%s", candidate);
        for(int i=0; i<argc-1; i++){
            if(strcmp(candidate, candidates[i].name) == 0){
                candidates[i].votes += 1;
            }
        }
    }
    int max_vote = 0;
    char winner[MAX];
    for(int i=0; i<argc-1; i++){
        if(max_vote < candidates[i].votes){
            max_vote = candidates[i].votes;
            strcpy(winner, candidates[i].name);
        }
    }
    printf("%s\n max vote: %d\n", winner, max_vote);
    return 0;
}