package com.task2;
public class larger {

        public static int largest(int a, int b, int c) {
            return Math.max(a, Math.max(b, c));
        }

        public static void main(String[] args) {
            // Test the method
            System.out.println("Largest: " + largest(10, 25, 7));
            System.out.println("Largest: " + largest(-5, -2, -9));
            System.out.println("Largest: " + largest(100, 100, 50));
        }
    }