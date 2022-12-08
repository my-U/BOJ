package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11720_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        char[] arr = input.readLine().toCharArray();
        int sum = 0;

        for(int i = 0; i < N; i++){
            int num = arr[i] - 48;
            sum += num;
        }
        System.out.println(sum);
    }
}
