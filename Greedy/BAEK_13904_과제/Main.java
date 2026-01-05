package Greedy.BAEK_13904_과제;

// N개의 과제 (1<=N<=1000)
// 점수가 높은 것부터 하나씩 빼오기
// 해당 기간 이하 날짜에 자리가 있다면 넣어주고
// 없다면 패스

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static class Task implements Comparable<Task> {
        int d, w;

        public Task(int d, int w) {
            this.d = d;
            this.w = w;
        }
        // 점수 높은 것 우선
        @Override
        public int compareTo(Task o) {
            return o.w - this.w;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<Task> list = new ArrayList<>();
        // 최장 과제 기간
        int maxDay = 0;

        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            list.add(new Task(d,w));
            maxDay = Math.max(maxDay,d);
        }

        Collections.sort(list);

        boolean[] used = new boolean[maxDay+1];
        int totalScore = 0;

        for (Task t : list) {
            // 가장 점수 높은 것부터
            // 해당 날짜 이하에 자리 있다면 넣기
            for (int i = t.d; i>0; i--) {
                if (!used[i]) {
                    used[i] = true;
                    totalScore += t.w;
                    break;
                }
            }
        }
        System.out.println(totalScore);
    }
}