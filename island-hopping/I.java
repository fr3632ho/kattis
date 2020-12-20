import java.util.*;
import java.io.*;

public class I {
  int m;


  public static void main(String[] args) {
    new I().run();
  }

  public void run() {
    Scanner scan = new Scanner(System.in);
    int t = Integer.parseInt(scan.nextLine());
    while(t-- > 0){
      m = Integer.parseInt(scan.nextLine());
      String[] line;
      double x,y;
      Point[] vals = new Point[m];
      for (int i=0; i<m;i++){
        line = scan.nextLine().split(" ");
        x = Double.parseDouble(line[0]);
        y = Double.parseDouble(line[1]);
        vals[i] = new Point(x, y, i);
      }

      PriorityQueue<Edge> edges = new PriorityQueue<Edge>();
      Set<Edge> seen = new HashSet<Edge>();
      for (Point a : vals) {
        for (Point b : vals) {
            Edge e = new Edge(a.dist(b), a.id, b.id);
            if (!seen.contains(e)) {
                edges.offer(e);
            }
        }
      }

      System.out.println(kruskal(edges, m));

    }
  }

  public void merge(int[] parents,int x, int y) {
    parents[find(parents, x)] = parents[find(parents, y)];
  }

  public int find(int[] parents, int a) {
    int root = a;
    while (root != parents[root]) root = parents[root];
    int p = a;
    while (a != root) {
      p = parents[a];
      parents[a] = root;
      a = p;
    }
    return root;
  }

  public double kruskal(PriorityQueue<Edge> edges, int n) {
    int[] parents = new int[n];
    int j = 0, e = 0;
    for (int i=0; i<n; i++){
      parents[i] = i;
    }

    double weight = 0;
    while (e < n-1) {
      Edge curr = edges.poll();
      int u, v;
      double w;
      w = curr.w;
      u = curr.u;
      v = curr.v;

      j++;
      int x = find(parents, u);
      int y = find(parents, v);
      if (x != y) {
        merge(parents, x, y);
        weight += w;
        e++;
      }
    }

    return weight;
  }

  class Edge implements Comparable<Edge> {
    int u, v;
    double w;

    public Edge(double w, int u, int v) {
      this.w = w;
      this.u = u;
      this.v = v;
    }

    @Override
    public boolean equals(Object o) {
      if (o instanceof Edge) {
        Edge e = (Edge) o;
        return (this.u == e.u && this.v == e.v)||(this.u == e.v && this.v == e.u);
      }
      return false;
    }

    @Override
    public int compareTo(Edge other) {
      double difference = this.w - other.w;
      if (difference > 0) return 1;
      if (difference == 0) return 0;
      return -1;
    }

    @Override
    public int hashCode() {
      return 31*u + v;
    }
  }

  class Point implements Comparable<Point> {
    double x, y;
    int id;

    public Point(double x, double y, int id){
      this.x=x;
      this.y=y;
      this.id = id;
    }

    @Override
    public boolean equals(Object other) {
      if (other instanceof Point){
          Point p2 = (Point) other;
          return this.id == p2.id;
      }
      return false;
    }

    @Override
    public int compareTo(Point other) {
      if (other.x != this.x) {
        return (int) (this.x - other.x);
      }
      return (int) (this.y - other.y);
    }

    public double dist(Point other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }

  }
}
