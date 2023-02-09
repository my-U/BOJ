package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _9093_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(input.readLine());
        
        for(int i = 0; i < T; i++){
            Stack<Character> stack = new Stack<>();
            String sentence = input.readLine() + ' '; // 단어 다음 띄어쓰기가 올 때 스택을 출력하기 때문에 마지막에 추가

            for(int j = 0; j < sentence.length(); j++) {
                if(sentence.charAt(j) == ' ') {
                    while(!stack.empty()) { // 스택에 문자가 존재하는 동안 실행
                        sb.append(stack.pop());
                    }
                    sb.append(' '); // 단어 사이 띄어쓰기 추가
                } else {
                    stack.add(sentence.charAt(j));
                }
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}
