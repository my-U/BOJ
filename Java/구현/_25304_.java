package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _25304_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(input.readLine());
        int N = Integer.parseInt(input.readLine());
        int total = 0;

        for(int i = 0; i < N; i++) {
            StringTokenizer str = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(str.nextToken());
            int b = Integer.parseInt(str.nextToken());

            total += a * b;
        }
        if (X == total) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
