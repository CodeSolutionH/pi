import javax.swing.*;

public class DataTypes {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Data Types");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Data Types in Java\n" +
            "public class DataTypes {\n" +
            "    public static void main(String[] args) {\n" +
            "        // Primitive Data Types\n" +
            "        byte myByte = 100;\n" +
            "        short myShort = 5000;\n" +
            "        int myInt = 100000;\n" +
            "        long myLong = 15000000000L;\n" +
            "        float myFloat = 5.75f;\n" +
            "        double myDouble = 19.99d;\n" +
            "        char myChar = 'A';\n" +
            "        boolean myBoolean = true;\n" +
            "\n" +
            "        // Non-Primitive Data Types\n" +
            "        String myString = \"Hello\";\n" +
            "        int[] myArray = {1, 2, 3};\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "Primitive Data Types: The basic building blocks of data in Java.\n" +
            "- byte, short, int, long: For whole numbers.\n" +
            "- float, double: For floating-point numbers.\n" +
            "- char: For single characters.\n" +
            "- boolean: For true/false values.\n\n" +
            "Non-Primitive Data Types: Also known as reference types.\n" +
            "- String: A sequence of characters.\n" +
            "- Array: A collection of elements of the same data type." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}