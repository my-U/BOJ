package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10871_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer str = new StringTokenizer(input.readLine());
        int N = Integer.parseInt(str.nextToken());
        int X = Integer.parseInt(str.nextToken());
        
        str = new StringTokenizer(input.readLine());
        for(int i = 0; i < N; i++) {
           int num = Integer.parseInt(str.nextToken());
            
           if(num < X) {
                sb.append(num).append(" ");
            }
        }
        System.out.println(sb);
    }
}