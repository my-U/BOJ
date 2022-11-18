package Java.구현;

import java.io.*;
import java.util.StringTokenizer;

public class _11022_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(input.readLine());

        for(int i = 1; i <= T; i++) {
            StringTokenizer str = new StringTokenizer(input.readLine());
            int A = Integer.parseInt(str.nextToken());
            int B = Integer.parseInt(str.nextToken());
            int sum = A + B;
            sb.append("Case #" + i + ": ").append(A).append(" + ").append(B).append(" = ").append(sum).append('\n');
            // sb.append("Case #")
            //     .append(i)
            //     .append(": ")
            //     .append(A)
            //     .append(" + ")
            //     .append(B)
            //     .append(" = ")
            //     .append(A+B)
            //     .append('\n');
            // 더 직관적일지도
            // 속도도 더 빠른 것 같음
        }
        System.out.println(sb);
    }
}
