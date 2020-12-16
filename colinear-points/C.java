import java.util.*;
import java.io.*;

public class C {

  static double EPS = 1e-12;

  public static void main(String[] args) {
    new C().run();
  }

  public void run() {
    Scanner scan = new Scanner(System.in);
    int n = Integer.parseInt(scan.nextLine());
    while (n != 0) {
      Point[] pts = new Point[n];
      String[] l;
      int x, y;
      for (int i=0; i<n; i++){
        l = scan.nextLine().strip().split(" ");
        x = Integer.parseInt(l[0]); y = Integer.parseInt(l[1]);
        pts[i] = new Point(x, y);
      }

      System.out.println(max_collinear_points(pts));

      n = Integer.parseInt(scan.nextLine());

    }
  }

  public double slope_and_intercept(Point a, Point b) {
    if (a.x == b.x) return Integer.MAX_VALUE;
    return (b.y - a.y)/(1.0 * (b.x - a.x));
  }

  public int max_collinear_points(Point[] pts) {
    int n = pts.length;
    int ans = n > 1 ? 2 : 1;
    if (ans < 2) return ans;

    for(int i = 0; i<n; i++) {
        Double[] slopes = new Double[n];
        int coinciding = 0;
        int end = 0;
        for(int j = 0; j<n; j++) {
            if (pts[i].x == pts[j].x && pts[i].y==pts[j].y){
              coinciding++;
              continue;
            }
            else {
                slopes[end] = slope_and_intercept(pts[i], pts[j]);
          }
          end++;
        }

        Arrays.sort(slopes, 0, end);
        for(int j=1, eqs=1; j < end; j++, eqs = 1) {
            while(j < end && Math.abs(slopes[j]-slopes[j-1] )< EPS) {
                j++;
                eqs++;
            }
            ans = Math.max(ans, eqs + coinciding);
        }
    }

    return ans;
  }

  class Point {
    int x, y;

    Point(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }


}
