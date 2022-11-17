package Java.구현;

import java.io.*;
import java.util.StringTokenizer;

public class _11021_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(input.readLine());

        for(int i = 1; i <= T; i++) {
            StringTokenizer str = new StringTokenizer(input.readLine());
            int sum = Integer.parseInt(str.nextToken()) + Integer.parseInt(str.nextToken());
        //     output.write("Case #" + i + ": " + sum);
        //     output.newLine();
            sb.append("Case #" + i + ": ").append(sum).append('\n');
        }
        // output.flush();
        // output.close();
        System.out.println(sb);

        // BufferedWriter가 System.out.println보다 속도가 더 빨라서 사용했지만 실행결과 더 느렸음
        // 더 빠른 것은 맞겠지만 문자열을 붙이는 과정에서 속도가 더 걸리는 것 같음
    }
}
