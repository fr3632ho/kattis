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

  int n, m;
  string s;
  unordered_map<string, int> freq_map;
  cin >> n >> m;
  rep(i, 0, n) {    
    rep(j, 0, m) {      
      cin >> s;
      freq_map[s] = freq_map[s] +  (freq_map[s] < i+1);      
    }
  }
  m = 0;
  vector<string> res;
  for (const pair<string, int> p : freq_map) {
    if (p.second == n) {
      m++;
      res.push_back(p.first);
    }
  }

  sort(res.begin(), res.end());
  cout << m << endl;
  for(string o : res) {
    printf("%s\n", o);
  }
  
  return 0;
}
