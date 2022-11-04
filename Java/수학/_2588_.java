package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2588_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(input.readLine());
        int y = Integer.parseInt(input.readLine());

        int a = x * (y % 10);
        int b = x * ((y / 10) % 10);
        int c = x * (y / 100);

        // String y = input.readLine();
        // char[] Y = y.toCharArray();
        // 문자열을 한 글자씩 쪼개서 char타입의 배열에 넣어주는 메소드
        
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(x * y);

        // System.out.println(x * (Y[2]-'0'));
        // System.out.println(x * (Y[1]-'0'));
        // System.out.println(x * (Y[0]-'0'));
        // System.out.println(x * Integer.parseInt(y));
    }
}
