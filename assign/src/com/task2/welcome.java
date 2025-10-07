package com.task2;
import java.util.Scanner;
public class welcome {
    public static String welcomeMessage(String name) {
        return "Hello " + name + ", Welcome to Java World!";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String userName = scanner.nextLine();

        String message = welcomeMessage(userName);
        System.out.println(message);

        scanner.close();
    }
}
