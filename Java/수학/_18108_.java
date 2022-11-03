package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _18108_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int year = Integer.parseInt(input.readLine());

        System.out.println(year - 543);
    }
}