package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _5597_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[31]; // 입력 가능한 숫자는 30까지이지만 인덱스를 30까지 가져야하기 때문에 배열 길이를 31로 설정함
        for(int i = 0; i < 28; i++) {
            int num = Integer.parseInt(input.readLine());
            arr[num] = 1;
        }
        for(int i = 1; i < 31; i++) {
            if(arr[i] != 1) System.out.println(i);
        }
    }
}