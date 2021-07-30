#include <stdio.h>
#include <stdlib.h>
// coins: 25, 10, 5, 1
double get_amount(void){
    double amount;
    do
    {
        printf("How much you are owed?");
        scanf("%lf", &amount);
    } while (amount < 0 || amount > 100);
    return amount;
}

int main(void){
    double amount = get_amount();
    //convert it to cent
    int cents = amount * 100;
    int most_coins[4] = {25, 10, 5, 1};
    int total_coin = 0;
    for(int i=0; i<4; i++){
        int num_coin = cents / most_coins[i];
        total_coin += num_coin;
        cents -= most_coins[i] * num_coin;
    }
    printf("%d\n", total_coin);
    return 0;
}