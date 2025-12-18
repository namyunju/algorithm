import java.util.*;
import java.io.*;

public class Solution {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			
			int[] dp = new int[K+1];
			
			for (int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				int v = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				
				for (int j=K; j>=v; j--) {
					if (dp[j] < dp[j-v]+c) {
						dp[j] = dp[j-v]+c;
					}
				}
			}
			System.out.println("#" + tc + " " + dp[K]);
		}
	}
}
