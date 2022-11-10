package Java.기하학;

import java.io.*;

public class _14681_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(input.readLine());
        int y = Integer.parseInt(input.readLine());

        if (x > 0 && y > 0) {
            System.out.println(1);
        } else if (x > 0 && y < 0) {
            System.out.println(4);
        } else if (x < 0 && y > 0) {
            System.out.println(2);
        } else System.out.println(3);
    }
}