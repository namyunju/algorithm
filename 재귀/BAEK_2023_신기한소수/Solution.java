import java.util.*;

class Solution {
    static int n;
    public static boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i=2; i*i <=num; i++) {
            if (num%i==0) return false;
        }
        return true;
    }

    public static void dfs(int num, int len) {
        if (len == n) {
            System.out.println(num);
            return;
        }
        for (int i=1; i<= 9; i++) {
            if (i%2 ==0) {
                continue;
            }
            int next_num = num*10+i;
            if (isPrime(next_num)) {
                dfs(next_num, len+1);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        dfs(2,1);
        dfs(3,1);
        dfs(5,1);
        dfs(7,1);
    }
}