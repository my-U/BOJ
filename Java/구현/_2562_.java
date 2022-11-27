package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2562_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        // 처음에 배열을 사용했는데 입력받을 때마다 값을 비교하면 돼서 변수를 사용함
        int max = 0, index = 0, num = 0;
        for(int i = 0; i < 9; i++) {
            num = Integer.parseInt(input.readLine());
            if(num > max) {
                max = num;
                index = i + 1;
            }
        }
        System.out.println(max);
        System.out.println(index);
    }
}