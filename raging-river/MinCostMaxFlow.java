import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.Arrays;


class MinCostMaxFlow {
    boolean found[];
    int N, dad[];
    long cap[][], flow[][], cost[][], dist[], pi[];

    static final long INF = Long.MAX_VALUE / 2 - 1;

    public static void main(String[] args) {
        int p, r, l;
        FastReader in = new FastReader();
        p = in.nextInt();
        r = in.nextInt();
        l = in.nextInt();
        long[][] cap = new long[r+4][r+4];
        long[][] cost = new long[r+4][r+4];
        cap[0][1] = p;
        cap[r+2][r+3] = p;
        for (int i=0; i<l; i++) {
            int n1, n2;
            n1 = in.nextInt();
            n2 = in.nextInt();
            n1 = change(n1, r);
            n2 = change(n2, r);

            cap[n1][n2]  = 1;
            cap[n2][n1]  = 1;
            cost[n1][n2] = 1;
            cost[n2][n1] = 1;
        }

        long[] res = new MinCostMaxFlow().mcmf(cap, cost, 0, r+3);
        //System.out.println(res[0] + " " + res[1]);

        if (res[0] >= p) {
            System.out.println(res[1]);
        } else {
            System.out.println(p-res[0] + " people left behind");
        }
    }

    static int change(int n, int r) {
        if (n==-2) {
            return 1;
        } else if(n==-1) {
            return r+2;
        } else {
            return n+2;
        }
    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
        }

        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }

        long nextLong() { return Long.parseLong(next()); }

        double nextDouble()
        {
            return Double.parseDouble(next());
        }

        String nextLine()
        {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    boolean search(int s, int t) {
        Arrays.fill(found, false);
        Arrays.fill(dist, INF);
        dist[s] = 0;

        while (s != N) {
          int best = N;
          found[s] = true;
          for (int k = 0; k < N; k++) {
            if (found[k]) continue;
            if (flow[k][s] != 0) {
              long val = dist[s] + pi[s] - pi[k] - cost[k][s];
              if (dist[k] > val) {
                dist[k] = val;
                dad[k] = s;
              }
            }
            if (flow[s][k] < cap[s][k]) {
              long val = dist[s] + pi[s] - pi[k] + cost[s][k];
              if (dist[k] > val) {
                dist[k] = val;
                dad[k] = s;
              }
            }

            if (dist[k] < dist[best]) best = k;
          }
          s = best;
        }
        for (int k = 0; k < N; k++)
          pi[k] = Math.min(pi[k] + dist[k], INF);
        return found[t];
    }

    long[] mcmf(long c[][], long d[][], int s, int t) {
        cap = c;
        cost = d;

        N = cap.length;
        found = new boolean[N];
        flow = new long[N][N];
        dist = new long[N+1];
        dad = new int[N];
        pi = new long[N];

        long totflow = 0, totcost = 0;
        while (search(s, t)) {
          long amt = INF;
          for (int x = t; x != s; x = dad[x])
            amt = Math.min(amt, flow[x][dad[x]] != 0 ?
            flow[x][dad[x]] : cap[dad[x]][x] - flow[dad[x]][x]);
          for (int x = t; x != s; x = dad[x]) {
            if (flow[x][dad[x]] != 0) {
              flow[x][dad[x]] -= amt;
              totcost -= amt * cost[x][dad[x]];
            } else {
              flow[dad[x]][x] += amt;
              totcost += amt * cost[dad[x]][x];
            }
          }
          totflow += amt;
        }

        return new long[]{ totflow, totcost };
    }
}
