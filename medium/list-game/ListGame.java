import java.util.*;
import java.io.*;

public class ListGame {

  public static void main(String[] args) {
    new ListGame();
  }

  public ListGame() {
    try {
      run();
    } catch (Exception e) {
      System.out.println("...");
    }
  }

  public void run() throws Exception {
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(scan.readLine());
    System.out.println(primeFactors(n));
  }

  public int primeFactors(int a) {
    List factors = new ArrayList();
    int p = 2; int n = a;
    while(p <= Math.sqrt(a)) {
      if((n % p) == 0){
        factors.add(p);
        n = n / p;
        continue;
      }
      p++;
    }
    return factors.size();
  }
}
