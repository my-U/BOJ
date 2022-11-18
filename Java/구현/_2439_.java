package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2439_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(input.readLine());

        for(int i = 1; i <= N; i++) {
            for(int j = N - i; j > 0; j--) {
                sb.append(" ");
            }
            for(int l = 1; l < i + 1; l++) {
                sb.append("*");
            }
        sb.append('\n');
        }
        // 8ms 만큼 시간 단축
        // for (int i=1; i <= N; i++) {
        //     sb.append(" ".repeat(N-i)); 공백을 N-i만큼 반복
        //     sb.append("*".repeat(i)); *을 i만큼 반복
        //     sb.append("\n");
    System.out.println(sb);
    }
}
