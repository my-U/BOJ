package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1110_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        int count = 0;
        int result = N;

        while(true) {
            N = (N % 10)*10 + ((N / 10) + (N % 10)) % 10;
            count += 1;
            if (N == result) break;
        }
        System.out.println(count);
    }
}