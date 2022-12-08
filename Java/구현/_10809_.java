package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _10809_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String s = input.readLine();

        int[] arr = new int[26];
        for(int i = 0; i < arr.length; i++){
            arr[i] = -1;
        }

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            
            if(arr[c - 'a'] == -1){
                // arr의 인덱스가 a~z순서이기 때문에 'a'를 뺌
                // 만약 c의 값이 a라면 c - 'a'의 값은 0임
                arr[c - 'a'] = i;
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i : arr){
            sb.append(i).append('\n');
        }
        System.out.print(sb);
    }
}