import javax.swing.*;

public class ClassesAndObjects {
    int x = 5;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Classes and Objects");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Classes and Objects in Java\n" +
            "public class ClassesAndObjects {\n" +
            "    int x = 5;\n" +
            "\n" +
            "    public static void main(String[] args) {\n" +
            "        ClassesAndObjects myObj = new ClassesAndObjects();\n" +
            "        System.out.println(myObj.x);\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "A class is a blueprint for creating objects.\n" +
            "An object is an instance of a class.\n" +
            "- `ClassesAndObjects myObj = new ClassesAndObjects();`: Creates an object of the `ClassesAndObjects` class.\n" +
            "- `myObj.x`: Accesses the `x` attribute of the `myObj` object." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}
