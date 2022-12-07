package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11654_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        char N = input.readLine().charAt(0); 
        // input.readLine은 String타입 이기 때문에 charAt을 사용하여 char타입으로 변환
        // 문자 하나만 입력받기 때문에 0번 인덱스
        int num = N;
        System.out.println(num);

        // 참고코드
        // int num = System.in.read(); System.in.read()는 기본적으로 아스키코드로 값을 받음
        // System.out.println(num);
    }
}