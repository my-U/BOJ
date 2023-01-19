package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1157_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[26];
        String S = input.readLine().toUpperCase(); // 대문자로 출력하기 위해 모두 대문자로 변환
        
        for(int i = 0; i < S.length(); i++){
            char C = S.charAt(i);
            arr[C - 'A'] += 1; // A의 아스키코드 숫자는 65
        }

        int max = -1;
        char answer = '?';
        for(int i = 0; i < arr.length; i++){
            if(max < arr[i]){
                max = arr[i];
                answer = (char)(i + 'A'); // i + A의 값을 문자로 변환
            } else if(max == arr[i]) { // 같은 값이 존재한 경우 2개 이상이기 때문에 ? 출력
                answer = '?';
            }
        }
        System.out.println(answer);
    }
}