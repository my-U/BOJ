package Java.수학;

 class _15596_ {
    long sum(int[] a){ // 정수 n에 대해선 고려하지 않는 듯함
        long sum = 0;
        for(int i = 0; i < a.length; i++){
            sum += a[i];
        }
        return sum;
    }
}
