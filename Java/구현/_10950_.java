package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10950_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < N; i++) {
            StringTokenizer str = new StringTokenizer(null);
            int A = Integer.parseInt(str.nextToken());
            int B = Integer.parseInt(str.nextToken());
            sb.append(A + B).append('\n');
        }
        System.out.println(sb);
    }
}
