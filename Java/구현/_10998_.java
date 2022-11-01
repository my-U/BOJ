package Java.구현;

import java.io.*;
import java.util.StringTokenizer;

public class _10998_{
    public static void main(String[] args)  throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());

        int A = Integer.parseInt(str.nextToken());
        int B = Integer.parseInt(str.nextToken());
        System.out.println(A * B);
    }
}
