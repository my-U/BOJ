package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10952_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int sum = 0;
        while(true) {
            StringTokenizer str = new StringTokenizer(input.readLine());
            int A = Integer.parseInt(str.nextToken());
            int B = Integer.parseInt(str.nextToken());
            sum = A + B;
            if(A == 0 && B == 0){
                break;
            }
            sb.append(sum).append('\n');
        }
    System.out.println(sb);
    // input.close();
    }
}