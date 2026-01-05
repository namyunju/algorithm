
package MST.BAEK_1414_불우이웃돕기;
// N개의 컴퓨터를 연결
// 각 컴퓨터 랜선 길이가 알파벳으로 주어짐
// 모든 컴퓨터를 연결 -> MST 
// 기부할 수 있는 랜선의 길이의 최댓값은?
// 모든 컴퓨터 연결 불가능할 시 -1 출력

// a~z : 1~26을 나타냄
// A~Z : 27~52를 나타냄
// 문자를 숫자로 변환하는 함수

// 아이디어
// N개 연결 최소 개수는 N-1개
// 최소 신장 트리 MST
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    static int[] parent;
    // 간선 클래스
    static class Edge {
        int u, v, weight;

        public Edge(int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        
        PriorityQueue<Edge> pq = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);

        int totalSum = 0; // 전체 랜선 길이 합

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                int w = charToInt(line.charAt(j));

                if (w == 0) continue; // 랜선 없음

                totalSum += w; // 일단 기부 가능 총액에 다 더함

                // 자기 자신이 아니고 연결된 경우만 MST 후보로 추가
                if (i != j) {
                    pq.add(new Edge(i, j, w));
                }
            }
        }

        int usedSum = 0;
        int count = 0; // 연결된 간선 개수

        while (!pq.isEmpty()) {
            Edge cur = pq.poll(); // 가장 짧은 랜선 꺼내기

            if (union(cur.u, cur.v)) {
                usedSum += cur.weight;
                count++;
            }
        }

       
        // N개의 컴퓨터를 연결하려면 최소 N-1개의 간선이 필요함 (N=1일 때는 0개)
        if (count == N - 1) {
            System.out.println(totalSum - usedSum);
        } else {
            System.out.println(-1);
        }
    }

    // 문자 -> 숫자 변환 함수 
    static int charToInt(char c) {
        if (c >= 'a' && c <= 'z') return c - 'a' + 1;
        if (c >= 'A' && c <= 'Z') return c - 'A' + 27;
        return 0;
    }

    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static boolean union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) return false;

        parent[rootB] = rootA;
        return true;
    }
}
// 클래스
// 관련 데이터를 하나로 묶어줌
// 위 문제에서는 랜선 정보를 저장할 때 3가지 데이터가 필요
// 출발, 도착, 길이
// 3 개의 변수를 따로 관리할 시 간선 정보가 막 섞여버림
// 세 변수를 한 세트로 묶어서 관리 -> 클래스
