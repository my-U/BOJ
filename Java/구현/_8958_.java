package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _8958_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(input.readLine());

        for(int i = 0; i < N; i++){
            char[] arr = input.readLine().toCharArray();
            int count = 0, sum = 0;
            for(int j = 0; j < arr.length; j++){
                if(arr[j] == 'O') {
                    count++;
                }
                else {
                    count = 0;
                }
                sum += count;
            }
            sb.append(sum).append('\n');
        }
        System.out.println(sb);
    }
}