#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, a, b) for (ll i = a; i < ll(b); i++)
#define ll long long
// compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
// undefined <filename.cpp>
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, c;
  cin >> n >> c;
  // Had that |xi - xj| - c|i - j|, j<=i
  // (xi-xj) - c(i - j) = xi - c*i - xj + c*j = xi - c*i + (-xj + c*j)
  // want to maximise xi - c*i + y, y = -xj + c*j
  // i.e. maximise y!
  ll ans[n];
  ll INF = (1 << 54);
  ll mpos = -INF, mneg = -INF, xi;
  for (ll i = 0; i < n; i++)
  {
    cin >> xi;
    mneg = max(mneg, -xi + c * i);
    mpos = max(mpos, xi + c * i);
    ans[i] = max(xi - c * i + mneg, -xi - c * i + mpos);
  }
  for (int i = 0; i < n - 1; i++)
  {
    cout << ans[i] << " ";
  }
  cout << ans[n - 1] << endl;
}
