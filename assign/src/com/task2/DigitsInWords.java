package com.task2;

import java.util.Scanner;

public class DigitsInWords {
    public static void printDigitsInWords(int number) {
        String[] words = {"Zero", "One", "Two", "Three", "Four",
                "Five", "Six", "Seven", "Eight", "Nine"};

        String numStr = String.valueOf(number);

        for (char digit : numStr.toCharArray()) {
            System.out.print(words[digit - '0'] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a 3-digit number: ");
        int num = scanner.nextInt();

        // Validation: check if number is 3-digit
        if (num >= 100 && num <= 999) {
            printDigitsInWords(num);
        } else {
            System.out.println("Please enter a valid 3-digit number!");
        }

        scanner.close();
    }
}

