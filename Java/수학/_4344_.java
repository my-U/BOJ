package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _4344_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int C = Integer.parseInt(input.readLine());
        
        for(int i = 0; i < C; i++){
            StringTokenizer str = new StringTokenizer(input.readLine());
            int N = Integer.parseInt(str.nextToken());
            int[] arr = new int[N];
            int sum = 0;
            int count = 0;
            for(int j = 0; j < N; j++){
                arr[j] = Integer.parseInt(str.nextToken());
                sum += arr[j];
            }
            for(int l = 0; l < N; l++){
                if(arr[l] > sum/N) count++;
            }
            double result = count * 100 / (double)N;
            sb.append(String.format("%.3f%%", result)).append('\n');
            
        }
        System.out.println(sb);
    }
}