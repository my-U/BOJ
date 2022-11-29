package Java.수학;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class _3052_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        // set을 사용하여 중복값 제거
        HashSet<Integer> hs = new HashSet<Integer>();

        for(int i = 0; i < 10; i++) {
            hs.add(Integer.parseInt(input.readLine()) % 42);
        }
        System.out.println(hs.size());
    }
}