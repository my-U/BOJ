package Java.브루트포스;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1065_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        int count = 0;

        for(int i = 1; i <= N; i++){
            if(i<=99){
                count += 1;
            }
            else{
                int num1 = i / 100, num2 = (i / 10) % 10, num3 = i % 10;
                if((num1 - num2) == (num2 - num3)){
                    count += 1;
                }
            }
        }
        System.out.println(count);
    }
}
