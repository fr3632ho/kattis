import java.util.*;
import java.io.*;

public class AllPairsPath {
  private int INF = 1000000000;

  public static void main(String[] args) {
    new AllPairsPath();
  }

  public AllPairsPath() {
    try {
      run();
    } catch (Exception e) {
      System.out.println("woops");
    }
  }

  public void floydWarshall(int[][] d, int n){
    for(int k=0; k<n;k++){
      for(int i=0; i<n;i++){
        for(int j=0; j<n;j++){
          if(d[i][k] != INF && d[k][j] != INF){
            d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
          }
        }
      }
    }

    // Negative Cycles
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        for(int k=0;k<n;k++){
          if(d[i][j] != -INF){
            if(d[k][k] < 0 && d[i][k] != INF && d[k][j] != INF){
              d[i][j] = -INF;
            }
          }
        }
      }
    }
  }

  public void run() throws Exception {
    int n, m, q, u, v, w;
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    String[] line = scan.readLine().split(" ");
    n = Integer.parseInt(line[0]); m = Integer.parseInt(line[1]); q = Integer.parseInt(line[2]);

    while(true) {
      int[][] matrix = new int[n][n];
      // Fill the matrix
      for(int i=0;i<n;i++) for(int j=0;j<n;j++) matrix[i][j] = (i==j) ? 0 : INF;

      // Create edge relations
      for(int i=0; i<m; i++){
        line = scan.readLine().split(" ");
        u = Integer.parseInt(line[0]); v = Integer.parseInt(line[1]);
        w = Integer.parseInt(line[2]);

        if(u == v)
          continue;

        if(matrix[u][v] > w)
          matrix[u][v] = w;

      }

      floydWarshall(matrix, n);

      for(int i=0; i<q;i++){
        line = scan.readLine().split(" ");
        u = Integer.parseInt(line[0]); v = Integer.parseInt(line[1]);

        int dist = matrix[u][v];
        if(dist == INF){
          System.out.println("Impossible");
        } else if (dist == -INF){
          System.out.println("-Infinity");
        } else {
          System.out.println(dist);
        }

      }
      line = scan.readLine().split(" ");
      n = Integer.parseInt(line[0]); m = Integer.parseInt(line[1]); q = Integer.parseInt(line[2]);
      if(n == 0){
        break;
      }
      System.out.println();

    }
  }
}
