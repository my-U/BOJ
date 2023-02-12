package Java.자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _9012_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(input.readLine());
        
        for(int i = 0; i < T; i++) {
            Stack<Character> stack = new Stack<>();
            String sentence = input.readLine();

            for(int j = 0; j < sentence.length(); j++) {
                if(sentence.charAt(j) == '('){
                    stack.push(sentence.charAt(j));
                } else {
                    if(!stack.isEmpty() && stack.peek() == '(') stack.pop();
                    else stack.push(sentence.charAt(j));
                }
            }
            if(stack.isEmpty()){
                sb.append("YES").append('\n');
            } else sb.append("NO").append('\n');
        }
        System.out.println(sb);
    }
}