
#include <string>
#include <iostream>

using namespace std;
typedef long long ll;
#define rep(i, a, b) for (ll i = a; i < ll(b); i++)
// compile with g++/cc -g -Wall -Wconversion -fsanitize=address,
// undefined <filename.cpp>
int main()
{
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  ll n, t, temp;
  cin >> t;
  while (t--)
  {
    string s;
    cin >> n >> s;
    int left = 0, right = 0, curr_len = s.length();
    for (int i = 0; i < n; i++)
    {
      if (4 > curr_len)
        break;

      if (i % 2 == 0)
      {
        left += curr_len / 4;
      }
      else
      {
        right += curr_len / 4;
      }
      curr_len -= curr_len / 4;
    }
    cout << s.substr(left, s.length() - right - left) << endl;
  }
}
