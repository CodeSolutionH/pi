import javax.swing.*;

public class Arrays {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Java Arrays");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 400);

        JTextArea textArea = new JTextArea(
            "// Arrays in Java\n" +
            "public class Arrays {\n" +
            "    public static void main(String[] args) {\n" +
            "        String[] cars = {\"Volvo\", \"BMW\", \"Ford\", \"Mazda\"};\n" +
            "        System.out.println(cars[0]); // Outputs Volvo\n" +
            "\n" +
            "        cars[0] = \"Opel\";\n" +
            "        System.out.println(cars[0]); // Outputs Opel\n" +
            "\n" +
            "        System.out.println(cars.length); // Outputs 4\n" +
            "    }\n" +
            "}\n\n" +
            "/* Explanation:\n" +
            "Arrays are used to store multiple values in a single variable.\n" +
            "- `String[] cars`: Declares an array of strings.\n" +
            "- `cars[0]`: Accesses the first element of the array (index is 0-based).\n" +
            "- `cars[0] = \"Opel\"`: Changes the value of the first element.\n" +
            "- `cars.length`: Returns the number of elements in the array." +
            "*/"
        );
        textArea.setEditable(false);
        frame.getContentPane().add(new JScrollPane(textArea));
        frame.setVisible(true);
    }
}
