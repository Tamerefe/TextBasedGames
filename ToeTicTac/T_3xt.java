import java.util.Scanner;

public class T_3xt {
    static char[][] board = {
            { ' ', ' ', ' ' },
            { ' ', ' ', ' ' },
            { ' ', ' ', ' ' }
    };

    public static void displayBoard() {
        System.out.print("");
        System.out.println("r/c 1   2   3");
        System.out.println("  -------------");
        for (int i = 0; i < 3; i++) {
            System.out.print((i + 1) + " | ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println("\n  -------------");
        }
    }

    public static boolean checkWinner(char player) {
        for (int i = 0; i < 3; i++) {
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
                    (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
                return true;
            }
        }
        if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
                (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
            return true;
        }
        return false;
    }

    public static boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == ' ') {
                    return false;
                }
            }
        }
        return true;
    }

    public static void playerMove(char player, Scanner sc) {
        int row, col;
        while (true) {
            System.out.print("Player " + player + ", enter row (1-3) and column (1-3): ");
            row = sc.nextInt() - 1;
            col = sc.nextInt() - 1;

            if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == ' ') {
                board[row][col] = player;
                break;
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char currentPlayer = 'X';
        boolean gameWon = false;

        while (!gameWon && !isBoardFull()) {
            displayBoard();
            playerMove(currentPlayer, sc);
            gameWon = checkWinner(currentPlayer);
            if (gameWon) {
                displayBoard();
                System.out.println("Player " + currentPlayer + " wins!");
            } else if (isBoardFull()) {
                displayBoard();
                System.out.println("It's a draw!");
            }
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }
        sc.close();
    }
}
