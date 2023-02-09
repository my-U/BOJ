package Java.자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10828_ {

    public static int[] stack; // 스택 배열
    public static int size = 0; // 원소 위치를 관리할 변수

    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(input.readLine());

        stack = new int[N];

        while(N > 0){
            st = new StringTokenizer(input.readLine(), " ");

            switch (st.nextToken()) {
                case "push":
                    push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    sb.append(pop()).append('\n');
                    break;
                case "size":
                    sb.append(size()).append('\n');
                    break;
                case "empty":
                    sb.append(empty()).append('\n');
                    break;
                case "top":
                    sb.append(top()).append('\n');
                    break;
                default:
                    break;
            }
            N--;
        }
        System.out.println(sb);

    }

    // push 메소드
    public static void push(int num){
        stack[size] = num;
        size++;
    }

    // pop 메소드
    public static int pop(){
        if(size == 0){
            return -1;
        } else {
            int ans = stack[size - 1];
            stack[size - 1] = 0;
            size--;
            return ans;
        }
    }

    // size 메소드
    public static int size(){
        return size;
    }

    // empty 메소드
    public static int empty(){
        if(size == 0) return 1;
        else return 0;
    }

    // top 메소드
    public static int top(){
        if(size == 0) return -1;
        else {
            int ans = stack[size - 1];
            return ans;
        }
    }
    
}