package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1546_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        StringTokenizer str = new StringTokenizer(input.readLine());
        int num = 0;
        int max = -1;
        float sum = 0;
        for(int i = 0; i < N; i++) {
            num = Integer.parseInt(str.nextToken());
            sum += num; 
            if(max < num) max = num;
        }
        
        System.out.println(sum / max * 100 / N);
    }
}