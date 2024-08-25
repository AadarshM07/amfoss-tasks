import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
 
class subtask2 {
 
    public static void main(String[] args)
    {

        try {

            FileReader fr = new FileReader("input.txt");
            FileWriter fw = new FileWriter("output.txt");
            String str = "";
            int i;
            while ((i = fr.read()) != -1) {
                str += (char)i;
            }
            System.out.println("Content of the file:");
            System.out.println(str);
            fw.write(str);
            fr.close();
            fw.close();
 
            // Display message
            System.out.println(
                "File reading and writing both done");
        }
 
        catch (IOException e) {
            System.out.println(
                "There are some IOException");
        }
    }
}
