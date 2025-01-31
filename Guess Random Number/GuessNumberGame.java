import java.util.Scanner;
import java.util.Random;

public class GuessNumberGame {
    public static void main(String[] args) {
        Scanner sys = new Scanner(System.in);
        Random random = new Random();

        while (true) {
            int randoms = random.nextInt(10);
            System.out.print("Enter a Number: ");
            int numb = sys.nextInt();

            System.out.println("The Number Was: " + randoms);

            if (numb == randoms) {
                System.out.println("Congratulations! You guessed the number!");
            } else {
                System.out.println("Unlucky! Better luck next time. Press Enter to continue or type 'exit' to quit.");
                sys.nextLine();
                String input = sys.nextLine();
                if (input.equalsIgnoreCase("exit")) {
                    break;
                }
            }
        }
        sys.close();
    }
}
