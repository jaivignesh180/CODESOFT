import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("hello") || userInput.equalsIgnoreCase("hi")) {
                System.out.println("Bot: Hello! How can I assist you today?");
            } else if (userInput.equalsIgnoreCase("how are you")) {
                System.out.println("Bot: I'm doing well, thanks! I'm a chatbot, so I don't have feelings like humans do.");
            } else if (userInput.equalsIgnoreCase("what is your name")) {
                System.out.println("Bot: My name is SimpleChatbot. I'm here to help answer your questions.");
            } else if (userInput.equalsIgnoreCase("quit") || userInput.equalsIgnoreCase("exit")) {
                System.out.println("Bot: Goodbye! It was nice chatting with you.");
                break;
            } else {
                System.out.println("Bot: I didn't understand that. Can you please rephrase your question?");
            }
        }
    }
}
