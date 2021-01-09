#include <iostream>
#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;


int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, m;
  cin >> n >> m;
  while (n != 0 && m != 0) {
    unordered_set<int> js;
    int q;
    for (int i=0;i<n;i++){
      cin >> q;
      js.insert(q);
    }
    int count;
    count = 0;
    for(int i=0; i<m;i++){
      cin >> q;
      if (js.count(q)) count++;
    }
    cout << count << '\n';
    cin >> n; cin >> m;
  }
  return 0;
}
