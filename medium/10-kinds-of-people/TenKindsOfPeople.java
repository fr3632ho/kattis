import java.util.*;
import java.io.*;

public class TenKindsOfPeople {
  private static int MAX1 = 1000;
  private static int[] parents = new int[MAX1*MAX1];
  private static int[] sizes = new int[MAX1*MAX1];
  private static int[][] grid = new int[MAX1][MAX1];
  private static int R, C;

  public static void main(String[] args) throws Exception {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    String[] line = scan.readLine().split(" ");

    R = Integer.parseInt(line[0]);
    C = Integer.parseInt(line[1]);

    // Fill parent vector & sizes
    for(int i=0;i<R*C;i++){
      parents[i] = i;
      sizes[i] = 1;
    }

    // Fill the grid
    for(int r=0, c=0; r<R; r++, c=0){
      for(char a : scan.readLine().toCharArray()){
        grid[r][c++] = (a - '0');
      }
    }

    //unionize
    for(int i=0;i<R;i++){
      for(int j=0;j<C;j++){
        if(j + 1 < C && grid[i][j] == grid[i][j+1]){
          union(i*C + j, i*C+j+1);
        }
        if (i + 1 < R && grid[i][j] == grid[i+1][j]){
          union(i*C + j, (i+1)*C + j);
        }
      }
    }


    int N = Integer.parseInt(scan.readLine().split(" ")[0]);
    for(int q=0; q<N;q++){
      line = scan.readLine().split(" ");
      int r1 = Integer.parseInt(line[0]) - 1, c1 = Integer.parseInt(line[1]) - 1;
      int r2 = Integer.parseInt(line[2]) - 1, c2 = Integer.parseInt(line[3]) - 1;

      int start = r1*C + c1, end = r2*C + c2;

      int root_one = find(start), root_two = find(end);

      if (find(start) == find(end)){
        if (grid[r1][c1] == 1) {
          System.out.println("decimal");
        } else {
          System.out.println("binary");
        }
      } else {
        System.out.println("neither");
      }
    }

  }

  // Think think think..
  public static void union(int a, int b){
    a = find(a); b = find(b);
    if (a == b) return;

    if (sizes[a] > sizes[b]) swap(a, b);
    sizes[a] += sizes[b];
    parents[b] = a;
  }

  public static int find(int a) {
    int root = a;

    while(root != parents[root]) root = parents[root];

    while(a != root){
      int _a = parents[a];
      parents[a] = root;
      a = _a;
    }
    return root;
  }

  public static void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
  }

}
