package Java.구현;

import java.io.*;
import java.util.StringTokenizer;

public class _1330_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());

        int A = Integer.parseInt(str.nextToken());
        int B = Integer.parseInt(str.nextToken());

        if (A < B) {
            System.out.println("<");
        }
        else if (A > B) {
            System.out.println(">");
        }
        else {
            System.out.println("==");
        }
        // System.out.println((a>b) ? (">") : ((a<b) ? ("<") : ("==")));
    }
}
