package Java.구현;

import java.io.*;
import java.util.StringTokenizer;

public class _1008_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());

        double A = Integer.parseInt(str.nextToken());
        double B = Integer.parseInt(str.nextToken());

        System.out.println(A / B);
    }
    
}
