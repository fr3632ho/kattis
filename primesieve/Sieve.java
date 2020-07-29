import java.util.*;
import java.io.*;

public class Sieve {

  private BitSet sieve;

  public static void main(String[] args) throws Exception {
    new Sieve();
  }

  public Sieve() throws Exception {
    run();
  }

  public int sieveOfEratosthenes(int n){
    sieve = new BitSet((n+1) / 2);
    int count = (n + 1) / 2;

    for (int i=3; i*i <= n; i += 2){
      if (isComposite(i)) {
        continue;
      }

      // Increment by two, skipping all even numbers
      for (int c = i * i; c <= n; c += 2 * i){
        if(!isComposite(c)){
          setComposite(c);
          count--;
        }
      }
    }

    return count;

  }

  public boolean isComposite(int k) {
    return sieve.get((k - 3) / 2); // Since we don't keep track of even numbers
  }

  public void setComposite(int k) {
    sieve.set((k - 3) / 2); // Since we don't keep track of even numbers
  }

  public boolean isPrime(int a) {
    if (a < 3)
      return a > 1;

    if (a == 2)
      return true;

    if ((a & 1) == 1)
      return !isComposite(a);
    else
      return false;

  }

  public void run() throws Exception{
    BufferedReader scan = new BufferedReader(new InputStreamReader(System.in));
    String[] line = scan.readLine().split(" ");

    int n = Integer.parseInt(line[0]); int q = Integer.parseInt(line[1]);
    System.out.println(sieveOfEratosthenes(n));

    for (int i=0; i < q; i++){
      line = scan.readLine().split(" ");
      System.out.println( isPrime(Integer.parseInt(line[0])) ? '1' : '0');
    }
  }

}
