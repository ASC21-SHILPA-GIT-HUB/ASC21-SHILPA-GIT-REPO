package com.task1;

public class WordCount {

    // Method to count only words (ignore numbers)
    static int countWordsOnly(String str) {
        if (str == null || str.isEmpty()) {
            return 0;
        }

        // Split by spaces
        String[] tokens = str.trim().split("\\s+");
        int count = 0;

        for (String token : tokens) {
            // Check if token contains only letters (ignore numbers)
            if (token.matches("[a-zA-Z]+")) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        String sentence = "Sum of 12 and 20 is 32";
        int wordCount = countWordsOnly(sentence);
        System.out.println("Number of words: " + wordCount);
    }
}