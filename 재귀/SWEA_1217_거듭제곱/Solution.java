package 재귀.SWEA_1217_거듭제곱;

import java.util.Scanner;
 
class Solution
{
    public static Integer solve(int N, int M, int now) {
        if (M == 0) {
            return now;
        }
        return solve(N, M-1, now*N);
    }
    public static void main(String args[]) throws Exception
    {   
        Scanner sc = new Scanner(System.in);
        int T = 10;
        for (int i=0; i<T; i++) {
            int tc = sc.nextInt();
            int N = sc.nextInt();
            int M = sc.nextInt();
 
            int ans = solve(N,M,1);
            System.out.println("#"+tc + " " + ans);
        }
        sc.close();
    }
}