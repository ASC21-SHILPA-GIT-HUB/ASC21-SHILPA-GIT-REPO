package com.demo.expection;
public class UnhandledExepction {
    public static void main(String[] args) {
        int i= 100;
        System.out.println("divide by zero");
        try {
            int result = i/0 ;
            System.out.println("result  "+ result);
        } catch (ArithmeticException e) {
            System.out.println("Exception caught: " + e.getMessage());
        }

    }
}
