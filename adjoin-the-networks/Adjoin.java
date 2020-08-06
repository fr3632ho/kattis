import java.util.*;
import java.io.*;

public class Adjoin {
  private boolean[] visited;
  private int[] dist, d;
  private List<List<Integer>> G;
  private int n, m, u, v;
  private int farthest, farthestIndex;
  private int op1, op2, op3;

  public static void main(String[] args) {
    new Adjoin();
  }

  public Adjoin() {
    try {
      run();
    } catch (IOException e) {
      System.out.println(e.getMessage());
    }
  }

  public Tuple BFS(int start) {

    dist = new int[n];
    for(int i=0; i<n;i++){
      dist[i] = -1;
    }
    dist[start] = 0;
    farthest = 0;
    farthestIndex = start;
    Deque<Integer> queue = new ArrayDeque();
    queue.push(start);
    while (!queue.isEmpty()) {
      u = queue.pollLast();
      visited[u] = true;
      List<Integer> neighBours = G.get(u);
      for(Integer i : neighBours) {
        if (dist[i] == -1) {
          dist[i] = dist[u] + 1;
          if (farthest < dist[i]) {
            farthest = dist[i];
            farthestIndex = i;
          }
          queue.addFirst(i);
        }
      }
    }
    return new Tuple(farthest, farthestIndex);
  }

  public int find(int a) {
    int root = a;
    while (root != d[root] && d[root] != -1) root = d[root];
    int _p;
    while (a != root) {
      _p = d[a];
      d[a] = root;
      a = _p;
    }
    return root;
  }

  public void join(int a, int b) {
    a = find(a); b = find(b);
    if(a==b) return;
    d[a] = b;
  }

  public int getLongestDist(int start) {
    return BFS(BFS(start).second()).first();
  }

  class Tuple {
    private int a, b;

    Tuple(int a,int b){
      this.a = a;
      this.b = b;
    }

    int first() {
      return this.a;
    }
    int second() {
      return this.b;
    }
  }

  public void run() throws IOException {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    String[] line = scan.readLine().split(" ");
    n = Integer.parseInt(line[0]); m = Integer.parseInt(line[1]);

    visited = new boolean[n]; d = new int[n];
    G = new ArrayList<>(n);
    for(int i=0; i<n; i++) {
      d[i] = -1; visited[i] = false;
      G.add(i, new ArrayList<>());
    }

    // Get queries
    for(int j=0; j<m; j++) {
      line = scan.readLine().split(" ");
      u = Integer.parseInt(line[0]); v = Integer.parseInt(line[1]);
      List<Integer> lOne = G.get(u); // Undirected
      List<Integer> lTwo = G.get(v);
      lOne.add(v); lTwo.add(u);
      G.add(u, lOne); G.add(v, lTwo);
      join(u, v);
    }

    Deque<Integer> lengths = new ArrayDeque();
    for(int i=0; i<n; i++) {
      if (!visited[i]) {
        if (d[i] != -1) {
          lengths.addLast(getLongestDist(i));
        }
        if (G.get(i).size() == 0) {
          lengths.addLast(0);
        }
      }
    }

    //Collections.sort(lengths);
    while(lengths.size() > 1) {
      n = lengths.peekLast() / 2; m = lengths.peekLast() / 2;
      if(lengths.peekLast() % 2 == 1) {
        n++;
      }
      lengths.pollLast();

      u = lengths.peekLast() / 2; m = lengths.peekLast() / 2;
      if (lengths.peekLast() % 2 == 1) {
        u++;
      }
      lengths.pollLast();

      op1 = n + m;
      op2 = u + v;
      op3 = n + u;
      lengths.addLast(Math.max(op1, Math.max(op2, op3)));
    }
    System.out.println(lengths.getFirst());

  }
}
