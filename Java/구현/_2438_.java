package Java.구현;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2438_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(input.readLine());

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < i + 1; j++) {
                sb.append("*");
            }
            sb.append('\n');
    //  sb.append('\n'); 앞으로 당기니 시간이 4ms 줄었음. 이유는 모르겠음. 사소한 부분으로도 실행시간이 많이 좌우되는 것 같음
        }
        System.out.println(sb);
    }
}
