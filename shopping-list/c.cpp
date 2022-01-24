#include <bits/stdc++.h>
#include <string>
#include <unordered_map>

using namespace std;
typedef long long ll;

#define rep(i,a,b) for (ll i = a; i<ll(b); i++)

//compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
//undefined <filename.cpp>
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  cout << setprecision(10);

  int n, t, d, i, out, t_prev, d_prev;
  cin >> n;
  t_prev = d_prev = out = 0;
  for (i = 0; i < n; i++) {
    cin >> t >> d;
    if (t==0) {
        continue;
    }
    out = max((d-d_prev)/(t-t_prev), out);
    t_prev = t; d_prev = d;
  }

  cout << out << endl;
  
  return 0;
}
