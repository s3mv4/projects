#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

int main() {
    
    int num;
    int guess;
    int range;
    bool range_active = true;
    bool game_active = true;
    bool again_active = true;
    char again;

    while (range_active) {
        srand(time(NULL));
        printf("How high would you like your number to be generated [>= 10] ");
        scanf("%d", &range);
        if (range >= 10) {
            num = rand() % range + 1;
            range_active = false;
        }
    }
    while (game_active) {
        scanf("%d", &guess);
        if (guess == num) {
            printf("Well done!\n");
            game_active = false;
        } else if (guess < num) {
            printf("Higher!\n");
        } else {
            printf("Lower!\n");
        }
    }
    while (again_active) {
        printf("Would you like to play again? [Y/n] ");
        scanf(" %c", &again);
        if (again == 'y' || again == 'Y') {
            main();
            again_active = false;
        } else if (again == 'n' || again == 'N') {
            again_active = false;
        }
    }

    return 0;
}
