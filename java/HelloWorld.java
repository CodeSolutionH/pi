import javax.swing.*;

public class HelloWorld {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Hello World");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JTextArea textArea = new JTextArea(
            "// Hello World in Java\n" +
            "public class HelloWorld {\n" +
            "    public static void main(String[] args) {\n" +
            "        System.out.println(\"Hello, World!\");\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "1.  `public class HelloWorld`: This declares a class named HelloWorld.\n" +
            "2.  `public static void main(String[] args)`: This is the main method where the program execution begins.\n" +
            "3.  `System.out.println(\"Hello, World!\")`: This prints the text \"Hello, World!\" to the console." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}