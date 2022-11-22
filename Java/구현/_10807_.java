package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10807_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        StringTokenizer str = new StringTokenizer(input.readLine());
        int[] arr = new int[N];
        int count = 0;
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(str.nextToken());
        }
        int serchNum = Integer.parseInt(input.readLine());
        for(int i = 0; i < N; i++) {
            if (arr[i] == serchNum) {
                count ++;
            }
        }
        System.out.println(count);
    }
}