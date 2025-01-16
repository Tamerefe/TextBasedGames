#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_CHARACTERS 23
#define ten 10

void init_random() {
    srand(time(NULL));
}

struct characters {
    char allcharacters[TOTAL_CHARACTERS][ten];
    char kiss[ten];
    char kill[ten];
    char marry[ten];
};

int main() {
    FILE *file;
    file = fopen("character.txt", "r");

    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    struct characters chars;

    for (int i = 0; i < TOTAL_CHARACTERS; i++) {
        if (fscanf(file, "%s", chars.allcharacters[i]) != 1) {
            printf("Error reading character data\n");
            fclose(file);
            return 1;
        }
    }

    fclose(file);
    init_random();

    int randomNum1, randomNum2, randomNum3;
    do {
        randomNum1 = rand() % TOTAL_CHARACTERS;
        randomNum2 = rand() % TOTAL_CHARACTERS;
        randomNum3 = rand() % TOTAL_CHARACTERS;
    } while (randomNum1 == randomNum2 || randomNum2 == randomNum3 || randomNum1 == randomNum3);

    printf("Welcome to Kill Kiss Marry (Valorant Edition)\n");
    printf("1. %s\n", chars.allcharacters[randomNum1]);
    printf("2. %s\n", chars.allcharacters[randomNum2]);
    printf("3. %s\n", chars.allcharacters[randomNum3]);

    int choice1, choice2, choice3;

    printf("Choose a character to Kiss (1, 2, or 3): ");
    scanf("%d", &choice1);

    if (choice1 < 1 || choice1 > 3) {
        printf("Invalid choice for Kiss.\n");
        return 1;
    }

    switch (choice1) {
        case 1:
            printf("Choose a character to Kill (2 or 3): ");
            scanf("%d", &choice2);
            if (choice2 == 2) {
                choice3 = 3;
            } else if (choice2 == 3) {
                choice3 = 2;
            } else {
                printf("Invalid choice for Kill.\n");
                return 1;
            }
            break;
        case 2:
            printf("Choose a character to Kill (1 or 3): ");
            scanf("%d", &choice2);
            if (choice2 == 1) {
                choice3 = 3;
            } else if (choice2 == 3) {
                choice3 = 1;
            } else {
                printf("Invalid choice for Kill.\n");
                return 1;
            }
            break;
        case 3:
            printf("Choose a character to Kill (1 or 2): ");
            scanf("%d", &choice2);
            if (choice2 == 1) {
                choice3 = 2;
            } else if (choice2 == 2) {
                choice3 = 1;
            } else {
                printf("Invalid choice for Kill.\n");
                return 1;
            }
            break;
        default:
            printf("Invalid choice.\n");
            return 1;
    }

    char *choices[3] = { chars.allcharacters[randomNum1], chars.allcharacters[randomNum2], chars.allcharacters[randomNum3] };

    snprintf(chars.kiss, sizeof(chars.kiss), "%s", choices[choice1 - 1]);
    snprintf(chars.kill, sizeof(chars.kill), "%s", choices[choice2 - 1]);
    snprintf(chars.marry, sizeof(chars.marry), "%s", choices[choice3 - 1]);

    printf("Character for Kiss: %s\n", chars.kiss);
    printf("Character for Kill: %s\n", chars.kill);
    printf("Character for Marry: %s\n", chars.marry);

    return 0;
}
