package Java.구현;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class _1000_ {
    public static void main(String[] args) throws IOException { 
        // InputOutputException의 약자로 입출력에 관련된 예외들을 처리함
        
        // Scanner의 사용법이 더 간단하지만 BufferedReader의 속도가 더 빨라 BufferedReader를 더 많이 사용함
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in)); // System.in은 표준 출력인 키보드를 의미
        // InputStreamReader는 버퍼의 크기, 어떤 디코더를 사용할지 등 입력에 필요한 데이터를 담고 있음
        // InputStreamReder를 BufferedReader의 매개변수로 넘겨주면, BufferedReader는 넘겨받은 InputStreamReader의 정보에 따라 같은 크기의 힙 버퍼와 Char 버퍼를 생성함(총 2개)
        // 이때, readLine을 통하여 사용자가 입력을 하면 heapbyBuffer에 아스키코드값을 저장함
        // 이후 저장해 두었던 디코더로 아스키코드를 Char 버퍼에 저장함
        // 저장한 버퍼내용을 하나의 String 형태로 만들어 사용자가 볼 수 있게 처리함

        // BufferedReader 클래스의 생성자는 기본 생성자가 존재하지 않음
        // System.in은 InputStream 타입이어서 BufferedReader의 생성자로 들어갈 수 없음
        // 때문에 InputStreamReader를 이용하여 System.in을 사용함

        String[] str = input.readLine().split(" "); // String 입력 시 readLine(), int 입력 시 read()

        int A = Integer.parseInt(str[0]); // int로 형 변환
        int B = Integer.parseInt(str[1]);
        System.out.println(A + B);
    }
}
