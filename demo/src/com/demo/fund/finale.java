package com.demo.fund;

final class A {
    void display() {
        System.out.println("Hello from class com.demo.fund.A");
    }
}
class B extends A {
    void show() {
        System.out.println("Hello from class com.demo.fund.B");
    }
}
public class finale {
    public static void main(String[] args) {
        B obj = new B();
        obj.display();
        obj.show();
    }
}
