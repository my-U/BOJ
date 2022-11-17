package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
// import java.io.BufferedWriter;
// import java.io.OutputStreamWriter;

public class _15552_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
        // BufferedReader가 Scanner와 유사하다면 BufferedWriter는 System.out.println과 유사함
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(input.readLine());

        for(int i = 0; i < T; i++) {
            StringTokenizer str = new StringTokenizer(input.readLine());
            int A = Integer.parseInt(str.nextToken());
            int B = Integer.parseInt(str.nextToken());
            int sum = A + B;
            sb.append(sum).append('\n');
        }
        System.out.println(sb);
        // output.write(sb.toString()); 출력할 내용을 담음. 콘솔에 출력은 안됨
        // output.flush(); 버퍼를 비워냄과 동시에 콘솔에 출력함
        // output.close(); 스트림을 닫음
    }
}