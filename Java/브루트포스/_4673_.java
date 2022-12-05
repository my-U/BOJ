package Java.브루트포스;

public class _4673_ {
    public static void main(String[] args) {
        boolean[] a = new boolean[10001];
        for(int i = 1; i < 10001; i++){
            int n = d(i);
            
            if(n < 10001) a[n] = true;
        }
        
        StringBuilder sb = new StringBuilder();

        for(int j = 1; j < 10001; j++){
            if(!a[j]) sb.append(j).append('\n');
        }
        System.out.println(sb);
    }
    public static int d(int number){
        int sum = number;
        
        while(number != 0){ // sum != 0 으로 썼었는데 시간초과가 뜸. 이유는 모르겠음
            sum += (number % 10);
            number = number / 10;
        }
        return sum;
    }
}