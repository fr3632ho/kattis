import java.util.*;
import java.io.*;

public class SPFA {
  private int n, m, q, s;
  private int u, v, w;
  private int inf = Integer.MAX_VALUE;
  private int[] dist, visits;
  private boolean[] inQueue, visited;

  public static void main(String[] args){
    new SPFA();
  }

  public SPFA(){
    try {
      run();
    } catch (IOException e){
      System.out.println(e.getMessage());
    }
  }

  public void run() throws IOException {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    String[] line = scan.readLine().split(" ");
    n = Integer.parseInt(line[0]); m = Integer.parseInt(line[1]);
    q = Integer.parseInt(line[2]); s = Integer.parseInt(line[3]);

    while(true){
      Map<Integer, List<Edge>> map = new HashMap<>();
      for(int i=0; i<m; i++){
        line = scan.readLine().split(" ");
        u = Integer.parseInt(line[0]);
        v = Integer.parseInt(line[1]);
        w = Integer.parseInt(line[2]);
        addEdge(map, u, v, w);
      }

      // Perform SPFA
      int[] distances = shortestFasterPath(map, s);

      for(int i=0; i<q; i++){
        int query = Integer.parseInt(scan.readLine());
        u = distances[query];
        if(u == -inf){
          System.out.println("-Infinity");
        } else if(u == inf){
          System.out.println("Impossible");
        } else {
          System.out.println(u);
        }
      }

      line = scan.readLine().split(" ");
      n = Integer.parseInt(line[0]); m = Integer.parseInt(line[1]);
      q = Integer.parseInt(line[2]); s = Integer.parseInt(line[3]);
      if(n == 0) break;

      System.out.println();

    }
  }

  public void DFS(Map<Integer, List<Edge>> map, int u, boolean[] visited){
    if(!visited[u]){
      visited[u] = true;
      if(map.get(u) != null){
        List<Edge> neighbours = map.get(u);
        for(Edge e : neighbours){
          DFS(map, e.getTo(), visited);
        }
      }
    }
  }

  public int[] shortestFasterPath(Map<Integer, List<Edge>> map, int source) {
    dist = new int[n];
    visits = new int[n];
    inQueue = new boolean[n];
    for(int i=0; i<n;i++){
      dist[i] = inf;
      visits[i] = 0;
      inQueue[i] = false;
    }
    dist[source] = 0; inQueue[source] = true;

    // Setup the queue
    Queue<Integer> queue = new ArrayDeque<>();
    queue.offer(source);
    while(!queue.isEmpty()){
      u = queue.poll();
      inQueue[u] = false;
      visits[u] += 1;

      if(visits[u] < n && map.get(u) != null){

        List<Edge> neighbours = map.get(u);
        for(int i=0; i< neighbours.size(); i++){
          Edge e = neighbours.get(i);
          v = e.getTo(); w = e.getWeight();
          if(dist[u] + w < dist[v]){
            dist[v] = dist[u] + w;
            if(!inQueue[v]){
              queue.offer(v);
              inQueue[v] = true;
            }
          }
        }
      }
    }

    // Reuse the old inQueue
    visited = inQueue;
    for(int i=0; i<n; i++) visited[i] = false;

    // All nodes with > n-1 relaxations
    for(int j=0; j<n; j++)
      if (visits[j] == n) DFS(map, j, visited);

    for(int h=0; h<n; h++)
      if(visited[h]) dist[h] = -inf;

    return dist;
  }

  public void addEdge(Map<Integer, List<Edge>> map, int from, int to, int weight){
    if (map.get(from) == null){
      map.put(from, new ArrayList<Edge>());
    }
    map.get(from).add(new Edge(to, weight));
  }

  class Edge {
    int to, weight;

    Edge(int to, int weight){
      this.to = to;
      this.weight = weight;
    }

    int getTo(){
      return this.to;
    }

    int getWeight(){
      return this.weight;
    }
  }
}
