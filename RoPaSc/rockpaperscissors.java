import java.util.Scanner;
import java.util.Random;

public class rockpaperscissors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] rps = { "Rock", "Paper", "Scissors" };

        while (true) {
            System.out.print("Enter move (Rock(r), Paper(p), Scissors(s)). To exit the game, type \"exit\": ");
            String playerMove = scanner.nextLine();

            if (playerMove.equalsIgnoreCase("exit")) {
                System.out.println("Game exited.");
                break;
            }

            String playerMoveFull = "";
            switch (playerMove.toLowerCase()) {
                case "r":
                    playerMoveFull = "Rock";
                    break;
                case "p":
                    playerMoveFull = "Paper";
                    break;
                case "s":
                    playerMoveFull = "Scissors";
                    break;
                default:
                    System.out.println("Invalid move, please try again.");
                    continue;
            }

            String computerMove = rps[random.nextInt(3)];
            System.out.println("Your move: " + playerMoveFull);
            System.out.println("Computer move: " + computerMove);

            if (playerMoveFull.equals(computerMove)) {
                System.out.println("It's a tie!");
            } else if ((playerMoveFull.equals("Rock") && computerMove.equals("Scissors")) ||
                    (playerMoveFull.equals("Paper") && computerMove.equals("Rock")) ||
                    (playerMoveFull.equals("Scissors") && computerMove.equals("Paper"))) {
                System.out.println("You win!");
            } else {
                System.out.println("You lose!");
            }
        }

        scanner.close();
    }
}
