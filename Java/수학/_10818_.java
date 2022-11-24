package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10818_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        StringTokenizer str = new StringTokenizer(input.readLine());
        StringBuilder sb = new StringBuilder();
        int max = -1000000;
        int min = 1000000;

        for(int i = 0; i < N; i++) {
            int a = Integer.parseInt(str.nextToken());
            if (max < a) {
                max = a;
            }
            if(min > a) {
                min = a;
            }
        }
        sb.append(min).append(" ").append(max);
        System.out.println(sb);
    }
}