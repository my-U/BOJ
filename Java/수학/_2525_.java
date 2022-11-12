package Java.수학;

import java.util.StringTokenizer;
import java.io.*;

public class _2525_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());
        StringBuilder sb = new StringBuilder();

        int h = Integer.parseInt(str.nextToken());
        int m = Integer.parseInt(str.nextToken());
        int time = Integer.parseInt(input.readLine());

        // 미리 연산 후 넣으면 시간이 더 단축됨
        // m += time
        // h += m / 60

        if (m + time < 60) {
            sb.append(h).append(" ").append(m + time);
        } else {
            if (h + ((m + time) / 60) >= 24) {
                sb.append(h + ((m + time) / 60) - 24).append(" ").append((m + time) % 60);
            } else {
                sb.append(h + ((m + time) / 60)).append(" ").append((m + time) % 60);
            }
        }

        System.out.println(sb);
    }
}
