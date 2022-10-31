package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1001_ {
    public static void main(String[] args) throws IOException{
        
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        String[] br = input.readLine().split(" ");
        // StringTokenizer br = new StringTokenizer(input.readLine()); 또는
        // StringTokenizer br = new StringTokenizer(input.readLine(), " "); 
        // 주어진 문자열을 지정한 구분자로 분리해주는 클래스
        // 지정한 구분자가 없다면 기본 구분자로 분리함

        int A = Integer.parseInt(br[0]);
        int B = Integer.parseInt(br[1]);
        // int A = Integer.parseInt(br.nextToken());
        // 분리된 문자열을 Token이라고 함
        // nextElement()는 Object를 반환, nextToken()은 String을 반환함
        
        System.out.println(A - B);
    }
}
