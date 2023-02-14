package Java.자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _1874_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<Integer> stack = new Stack<>();
        int t = 0;
        int n = Integer.parseInt(input.readLine());

        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(input.readLine());

            if(t < num){
                for(int j = t + 1; j <= num; j++) {
                    stack.push(j);
                    sb.append("+").append("\n");
                }
                t = num;
            } else if(stack.peek() != num) { // 입력받은 값이 t의 값보다 크지 않다면 n보다 작은 수인데, 스택의 마지막 원소와 입력된 값이 일치하지 않는다면 수열이 불가능함 
                    System.out.println("NO");
                    return; // 종료
            }
            stack.pop();
            sb.append("-").append("\n");
        }
        System.out.println(sb);
    }
}