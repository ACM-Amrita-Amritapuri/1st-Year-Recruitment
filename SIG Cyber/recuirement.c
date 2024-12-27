#include <stdio.h>
#include <string.h>

int wrong_choice(char input[], char superkey[]);

int game() {
    char input[10]; 
    char superkey[] = "863426";  
    
    printf("The machine needs to play a game to reveal a flag\nEnter 1 for Rock, 2 for Paper, and 3 for Scissors\n");
    scanf("%s", input); 
    
    if (strcmp(input, "1") == 0 || strcmp(input, "2") == 0 || strcmp(input, "3") == 0) {
       
        int num_input = input[0] - '0'; 
        int choice = num_input % 3 + 1;
        
        printf("Computer Choice is: ");
        if (choice == 1) {
            printf("Rock\n");
        } else if (choice == 2) {
            printf("Paper\n");
        } else if (choice == 3) {
            printf("Scissors\n");
        }
        printf(" Computer won\n");
    } else if (strcmp(input, superkey) != 0) {
        printf(" Invalid input\n");
        printf(" Hint:Every Thing is Characteristed \n (char)int-(char)int=int(char)");
    }

   
    if (strcmp(input, superkey) == 0) {
        wrong_choice(input, superkey);
    }
    
    return 0;
}

int wrong_choice(char input[], char superkey[]) {
    if (strcmp(input, superkey) == 0) {
        char hex_array[15] = {0x42, 0x44, 0x4e, 0x7c, 0x73, 0x34, 0x77, 0x34, 0x32, 0x33, 0x36, 0x32, 0x6f, 0x68, 0x7e};
        int str_len = 15;
        for (int i = 0; i < str_len; i++) {
            printf("%c", hex_array[i] - 1);
        }
    printf("\n");
    }
    return 0;
}

int main() {
    game();

    return 0;
}
