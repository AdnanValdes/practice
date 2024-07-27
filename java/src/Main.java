package src;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Hello World 2!");

        // datatypes
        int hello_world = 5;
        double num2 = 5.0;
        boolean b = true;
        char c = 't';
        String str = "my string";
        
        System.out.println(hello_world);

        int p;
        p = 6;
        System.out.println(p);

        // operations
        int x, y, z, sum;
        x = 7; y = 6; z = 56;
        sum = x % y / z;
        System.out.println(sum);

        // typecasting
        double u = x / y;
        System.out.println(u);
        u = x / (double) y;
        System.out.println(u);

        // input
        Scanner sc = new Scanner(System.in);
        // Note that 'next()' only gets the next space-separated token, so a full
        // sentence will not work.
        String scanned = sc.next();
        System.out.println(scanned);

        // To get ints from a user we must do as follows
        int scanned2 = sc.nextInt();
        System.out.println(scanned2);

        // We can also avoid many errors by converting a string into an int:
        int converted = Integer.parseInt(scanned);
        System.out.println(converted);

        // Using booleans and conditionals
        // < > == <= >= !=
        boolean compare = x < y;
        System.out.println(compare);

        String h = "hello";
        String H = "HELLO";

        compare = h == H; // Note that when comparing string we should use s.equals("String")
        System.out.println(compare);

        // Chaining comparisons
        compare = x > y && z <y; // AND operator
        compare = x > y || z <y; // OR operator 
        compare = !(x > y || z <y); // NOT operator

        // If, Else, Elseif

    }
}

