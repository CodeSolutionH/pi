import javax.swing.*;

public class IfElse {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java If-Else");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// If-Else in Java\n" +
            "public class IfElse {\n" +
            "    public static void main(String[] args) {\n" +
            "        int time = 20;\n" +
            "        if (time < 18) {\n" +
            "            System.out.println(\"Good day.\");\n" +
            "        } else {\n" +
            "            System.out.println(\"Good evening.\");\n" +
            "        }\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "The `if` statement executes a block of code if a specified condition is true.\n" +
            "The `else` statement executes a block of code if the same condition is false.\n" +
            "In this example, since `time` is 20 (which is not less than 18), the `else` block is executed." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}
