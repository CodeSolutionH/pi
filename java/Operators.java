import javax.swing.*;

public class Operators {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Operators");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Operators in Java\n" +
            "public class Operators {\n" +
            "    public static void main(String[] args) {\n" +
            "        int x = 10;\n" +
            "        int y = 5;\n" +
            "\n" +
            "        // Arithmetic Operators\n" +
            "        System.out.println(\"x + y = \" + (x + y)); // Addition\n" +
            "        System.out.println(\"x - y = \" + (x - y)); // Subtraction\n" +
            "        System.out.println(\"x * y = \" + (x * y)); // Multiplication\n" +
            "        System.out.println(\"x / y = \" + (x / y)); // Division\n" +
            "        System.out.println(\"x % y = \" + (x % y)); // Modulus\n" +
            "\n" +
            "        // Relational Operators\n" +
            "        System.out.println(\"x > y is \" + (x > y)); // Greater than\n" +
            "        System.out.println(\"x < y is \" + (x < y)); // Less than\n" +
            "\n" +
            "        // Logical Operators\n" +
            "        boolean a = true;\n" +
            "        boolean b = false;\n" +
            "        System.out.println(\"a && b is \" + (a && b)); // Logical AND\n" +
            "        System.out.println(\"a || b is \" + (a || b)); // Logical OR\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "Arithmetic Operators: Used to perform mathematical calculations.\n" +
            "Relational Operators: Used to compare two values.\n" +
            "Logical Operators: Used to combine conditional statements." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}