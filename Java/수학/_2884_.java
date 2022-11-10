package Java.수학;

import java.io.*;
import java.util.StringTokenizer;

public class _2884_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());
        StringBuilder sb = new StringBuilder();

        int h = Integer.parseInt(str.nextToken());
        int m = Integer.parseInt(str.nextToken());

        if (m >= 45) {
            sb.append(h).append(" ");
            sb.append(m - 45);
        } else {
            if (h == 0) {
                sb.append(23).append(" ");
                sb.append(m + 15);
            } else {
                sb.append(h - 1).append(" ");
                sb.append(m + 15);
            }
        }

        System.out.println(sb);
    }
}