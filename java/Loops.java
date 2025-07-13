import javax.swing.*;

public class Loops {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Loops");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Loops in Java\n" +
            "public class Loops {\n" +
            "    public static void main(String[] args) {\n" +
            "        // For Loop\n" +
            "        System.out.println(\"For Loop:\");\n" +
            "        for (int i = 0; i < 5; i++) {\n" +
            "            System.out.println(i);\n" +
            "        }\n" +
            "\n" +
            "        // While Loop\n" +
            "        System.out.println(\"While Loop:\");\n" +
            "        int i = 0;\n" +
            "        while (i < 5) {\n" +
            "            System.out.println(i);\n" +
            "            i++;\n" +
            "        }\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "For Loop: Executes a block of code a specified number of times.\n" +
            "While Loop: Executes a block of code as long as a specified condition is true." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}
