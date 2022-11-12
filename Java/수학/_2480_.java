package Java.수학;

import java.io.*;
import java.util.StringTokenizer;

public class _2480_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());

        int A = Integer.parseInt(str.nextToken());
        int B = Integer.parseInt(str.nextToken());
        int C = Integer.parseInt(str.nextToken());
        int m = 0;

        if (A == B && A == C && B == C) {
            m = 10000 + A * 1000;
        } else if (A == B || A == C) {
            m = 1000 + A * 100;
        } else if (B == C) {
            m = 1000 + B * 100;
        } else {
            m = 100 * Math.max(A, Math.max(B, C));            
        }

        System.out.println(m);
    }
}
