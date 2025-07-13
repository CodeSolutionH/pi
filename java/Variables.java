import javax.swing.*;

public class Variables {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Variables");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        JTextArea textArea = new JTextArea(
            "// Variables in Java\n" +
            "public class Variables {\n" +
            "    public static void main(String[] args) {\n" +
            "        String name = \"John\";      // String\n" +
            "        int age = 25;               // Integer\n" +
            "        double salary = 50000.50;   // Double\n" +
            "        boolean isStudent = true;   // Boolean\n" +
            "\n" +
            "        System.out.println(\"Name: \" + name);\n" +
            "        System.out.println(\"Age: \" + age);\n" +
            "        System.out.println(\"Salary: \" + salary);\n" +
            "        System.out.println(\"Is Student: \" + isStudent);\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "1.  `String name = \"John\"`: Declares a variable `name` of type String and assigns it the value \"John\".\n" +
            "2.  `int age = 25`: Declares a variable `age` of type int and assigns it the value 25.\n" +
            "3.  `double salary = 50000.50`: Declares a variable `salary` of type double and assigns it the value 50000.50.\n" +
            "4.  `boolean isStudent = true`: Declares a variable `isStudent` of type boolean and assigns it the value true." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}