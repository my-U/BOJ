package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2675_{
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(input.readLine());
        StringTokenizer str;

        for(int i = 0; i < T; i++){
            str = new StringTokenizer(input.readLine());
            int R = Integer.parseInt(str.nextToken());
            String S = str.nextToken();

            for(int j = 0; j < S.length(); j++){
                for(int l = 0; l < R; l++){
                    sb.append(S.charAt(j));
                }
            }
            sb.append(' ');
        }
        System.out.println(sb);
    }
}