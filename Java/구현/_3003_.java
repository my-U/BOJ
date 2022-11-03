package Java.구현;

import java.io.*;
import java.util.*;

public class _3003_ {
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer str = new StringTokenizer(input.readLine());

        int king = Integer.parseInt(str.nextToken());
        int queen = Integer.parseInt(str.nextToken());
        int rook = Integer.parseInt(str.nextToken());
        int bishop = Integer.parseInt(str.nextToken());
        int knight = Integer.parseInt(str.nextToken());
        int pawn = Integer.parseInt(str.nextToken());

        System.out.print(1 - king + " ");
        System.out.print(1 - queen + " ");
        System.out.print(2 - rook + " ");
        System.out.print(2 - bishop + " ");
        System.out.print(2 - knight + " ");
        System.out.print(8 - pawn + " ");
    }
}
