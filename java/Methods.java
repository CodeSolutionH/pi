import javax.swing.*;

public class Methods {
    static void myMethod() {
        System.out.println("I just got executed!");
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Methods");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Methods in Java\n" +
            "public class Methods {\n" +
            "    static void myMethod() {\n" +
            "        System.out.println(\"I just got executed!\");\n" +
            "    }\n" +
            "\n" +
            "    public static void main(String[] args) {\n" +
            "        myMethod();\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "A method is a block of code which only runs when it is called.\n" +
            "- `static void myMethod()`: Defines a method named `myMethod`.\n" +
            "- `myMethod()`: Calls the `myMethod` method." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}
