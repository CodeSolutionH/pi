import javax.swing.*;

public class Constructors {
    int x;

    public Constructors() {
        x = 5;
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Constructors");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Constructors in Java\n" +
            "public class Constructors {\n" +
            "    int x;\n" +
            "\n" +
            "    public Constructors() {\n" +
            "        x = 5;\n" +
            "    }\n" +
            "\n" +
            "    public static void main(String[] args) {\n" +
            "        Constructors myObj = new Constructors();\n" +
            "        System.out.println(myObj.x);\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "A constructor is a special method that is used to initialize objects.\n" +
            "- `public Constructors()`: Defines a constructor for the `Constructors` class.\n" +
            "- The constructor is called when an object of the class is created." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}