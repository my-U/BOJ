package Java.구현;

import java.io.*;

public class _2739_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(input.readLine());

        for(int i = 1; i < 10; i++) {
            System.out.println(N + " * " + i + " = " + i * N);
        }
        // StringBuilder로 연결 후 출력하면 시간은 단축되고 메모리는 덜 사용됨
        // StringBuilder sb = new StringBuilder();
        // for (int i = 1; i < 10; i++) {
        //     sb.append(N).append(" * ").append(i).append(" = ").append(N * i).append('\n');
        // }
        // System.out.println(sb);
    }
}