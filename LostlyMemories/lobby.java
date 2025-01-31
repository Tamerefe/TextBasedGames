import java.util.Scanner;

public class lobby {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("\033[1;34m"); // Set text color to blue
        System.out.println("****************************************");
        System.out.println("*                                      *");
        System.out.println("*      Welcome to Lostly Memories!     *");
        System.out.println("*                                      *");
        System.out.println("****************************************");
        System.out.println("\033[0m"); // Reset text color

        System.out.println("\033[1;33mSelect Language / Dil Seçiniz: (1: English / 2: Türkçe)\033[0m");
        System.out.print(">> ");
        int languageChoice = scanner.nextInt();
        scanner.nextLine(); // Buffer clearing

        if (languageChoice == 1) {
            storyenglish.startGameEnglish(scanner);
        } else if (languageChoice == 2) {
            storyturkish.startGameTurkish(scanner);
        } else {
            System.out.println("\033[1;31mInvalid selection. Defaulting to English.\033[0m");
            storyenglish.startGameEnglish(scanner);
        }

        scanner.close();
    }
}