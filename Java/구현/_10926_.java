package Java.구현;

import java.io.*;

public class _10926_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        // StringBuilder StringBuilder = new StringBuilder(input.readLine());
        // String은 소위 불변 객체라고 함
        // 그래서 하나의 문자열에 다른 문자열을 연결하면 새 문자열이 생성되고, 이전 문자열은 가비지 컬렉터로 들어감
        // 또한 String 객체와 String 객체를 더하는 행위는 메모리 할당과 메모리 해제를 발생시켜 비효율적인 코드가 됨
        // StringBuilder는 새로운 객체를 생성하는 것이 아닌 기존의 데이터에 더하는 방식이기 때문에 속도도 빠르며 상대적으로 부하가 적음
        
        System.out.println(input.readLine() + "??!");
        // StringBuilder.append("??!");
        // append()로 문자열을 추가함

        // System.out.println(StringBuilder.toString());
        // 출력하거나 String 변수에 값을 넣을 때 toString()을 사용한다.
        
    }
}
