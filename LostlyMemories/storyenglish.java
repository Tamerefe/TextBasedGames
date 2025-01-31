import java.util.Scanner;

public class storyenglish {
    public static void startGameEnglish(Scanner scanner) {

        System.out.println("\033[1;33mWhat is your name?\033[0m");
        System.out.print(">> ");
        String playerName = scanner.nextLine();

        System.out.println("\n\033[1;32mHello, " + playerName
                + ". You wake up in a dark forest with no memory of who you are.\033[0m");
        System.out.println(
                "\033[1;32mIn front of you, there are two paths: one is a misty trail, the other is an old stone bridge.\033[0m");
        System.out.println("\033[1;33mWhich path do you choose?\033[0m (1: Misty Trail / 2: Stone Bridge)");

        System.out.print(">> ");
        int choice = scanner.nextInt();
        scanner.nextLine();

        if (choice == 1) {
            mistyPathEnglish(scanner);
        } else if (choice == 2) {
            stoneBridgeEnglish(scanner);
        } else {
            System.out.println("\033[1;31mInvalid choice. The shadows consume you...\033[0m");
        }
    }

    public static void mistyPathEnglish(Scanner scanner) {
        System.out.println("\033[1;32mYou walk along the misty trail, barely able to see your surroundings.\033[0m");
        System.out.println(
                "\033[1;32mSuddenly, an old cabin appears before you. Do you want to enter?\033[0m (1: Yes / 2: No)");

        System.out.print(">> ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println(
                    "\033[1;32mYou step inside the cabin and find an ancient book. As you open it, memories start flooding back...\033[0m");
            System.out.println(
                    "\033[1;32mThe book describes a hidden temple in the heart of the forest. Do you follow the clues?\033[0m (1: Yes / 2: No)");
            System.out.print(">> ");
            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println(
                        "\033[1;32mYou journey deeper into the forest, encountering strange symbols and ruins.\033[0m");
                System.out.println("\033[1;32mYou find the temple, but a shadowy guardian blocks the entrance.\033[0m");
                System.out.println(
                        "\033[1;33mDo you challenge the guardian or attempt to sneak past?\033[0m (1: Challenge / 2: Sneak)");
                System.out.print(">> ");
                choice = scanner.nextInt();

                if (choice == 1) {
                    System.out.println(
                            "\033[1;32mYou fight bravely and defeat the guardian. Inside, you find pictures of your family and writings about your identity. Do you follow these clues?\033[0m (1: Follow / 2: Burn the Pictures)");
                    System.out.print(">> ");
                    choice = scanner.nextInt();
                    if (choice == 1) {
                        System.out.println(
                                "\033[1;32mThe clues lead you to an island where you find your lost memories and identity. You win!\033[0m");
                        System.out.println("\033[1;32mYou win!\033[0m");
                    } else {
                        System.out.println(
                                "\033[1;31mYou burn the pictures and the temple collapses. The shadows consume you and you are lost forever...\033[0m");
                        System.out.println("\033[1;31mGame Over.\033[0m");
                    }
                } else {
                    System.out.println(
                            "\033[1;31mYou try to sneak in but fail. The guardian banishes you to the shadows...\033[0m");
                    System.out.println("\033[1;31mGame Over.\033[0m");
                }
            } else {
                System.out.println(
                        "\033[1;31mYou ignore the clues and leave the cabin. The shadows eventually find you...\033[0m");
                System.out.println("\033[1;31mGame Over.\033[0m");
            }
        } else {
            System.out.println(
                    "\033[1;31mYou decide not to enter and move away. However, the shadows consume you...\033[0m");
            System.out.println("\033[1;31mGame Over.\033[0m");
        }
    }

    public static void stoneBridgeEnglish(Scanner scanner) {
        System.out
                .println("\033[1;32mAs you cross the old stone bridge, a shadowy figure appears in the middle.\033[0m");
        System.out.println(
                "\033[1;32mThe figure asks you who you are. If you answer incorrectly, the bridge will collapse.\033[0m");
        System.out.println("\033[1;33mWhat is your answer?\033[0m (1: The Unknown Wanderer / 2: Shadow Hunter)");

        System.out.print(">> ");
        int choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println(
                    "\033[1;32mThe shadow nods as if recognizing you and vanishes. You safely cross the bridge and find a forgotten village.\033[0m");
            System.out.println(
                    "\033[1;32mThe villagers seem to know you. They take you to an elder who reveals your past.\033[0m");
            System.out.println(
                    "\033[1;33mDo you stay to learn more or continue your journey?\033[0m (1: Stay / 2: Continue)");
            System.out.print(">> ");
            choice = scanner.nextInt();

            if (choice == 1) {
                System.out.println(
                        "\033[1;32mThe elder reveals you are the lost guardian of the Shadow Realm! With these abilities, what will you do?\033[0m (1: Protect / 2: Destroy)");
                System.out.print(">> ");
                choice = scanner.nextInt();
                if (choice == 1) {
                    System.out.println(
                            "\033[1;32mYou protect the village and the people are grateful. You find your lost identity and become a true hero!\033[0m");
                    System.out.println("\033[1;32mYou win!\033[0m");
                } else {
                    System.out.println(
                            "\033[1;31mYou destroy the village and the shadows consume you. You are lost forever...\033[0m");
                    System.out.println("\033[1;31mGame Over.\033[0m");
                }
            } else {
                System.out.println(
                        "\033[1;31mYou continue your journey but the truth remains a mystery. You live in the shadows forever...\033[0m");
                System.out.println("\033[1;31mGame Over.\033[0m");
            }
        } else {
            System.out.println(
                    "\033[1;31mThe shadow perceives you as a threat and shatters the bridge! You fall into the abyss...\033[0m");
            System.out.println("\033[1;31mGame Over.\033[0m");
        }
    }
}