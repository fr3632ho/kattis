#include <vector>
#include <bits/stdc++.h>
#include <iostream>

using namespace std;
int n;

void prnt_rec(vector<vector<int> > &adj, vector<string> &v, int i){
    vector<int> out;
    out.push_back(i);
    while(out.size() > 0) {
        int node;
        node = out.back();
        cout << v[node];
        out.pop_back();
        for(int i=0;i<adj[node].size();i++){
            out.push_back(adj[node][adj[node].size()-1-i]);
        }
    }
    cout << endl;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);

  cin >> n;
  vector<string> strings(n);

  for(int i=0;i<n;i++){
      cin >> strings[i];
  }

  vector<vector<int> > adj;
  adj.assign(n, vector<int>());
  int last = -1;
  for(int i=0;i<n-1;i++){
      int a, b;
      cin >> a >> b;
      a--;b--;
      adj[a].push_back(b);
      last = a;
  }

  prnt_rec(adj, strings, last);
  cout.flush();
}
