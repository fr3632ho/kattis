#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <math.h>
#include <string>

using namespace std;

const double eps = 1e-9;
const int inf = 1e9;
int n;

struct city {
  int x;
  int y;
  string name;
  float dist;
};

struct point {
  int x;
  int y;
};

struct lkoef {
  int a, b, c;
};

lkoef make_lkoef(point c1, point c2) {
  lkoef line;
  line.b = c2.x - c1.x;
  line.a = c1.y - c2.y;
  line.c = c2.x*c1.y - c1.x*c2.y;
  return line;
}

float distance_to_line(lkoef l, city p) {
  l.c *=-1;
  float a,b;
  a = float( (l.a*p.x) + (l.b*p.y) + l.c);
  if(a<0) a*=-1;
  b = float(sqrt(l.a*l.a + l.b*l.b));
  l.c *= -1;
  return a/b;
}


int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n;
  point p1, p2;
  while(n--){
    cin >> p1.x >> p1.y >> p2.x >> p2.y;
    lkoef line = make_lkoef(p1, p2);
    // Line is now up to date
    int cities;
    float mindist = inf;
    cin >> cities;
    city c;
    mindist = inf;
    vector<city> ans;
    for (int i=0;i<cities;i++){
        cin >> c.name >>c.x >> c.y;
        float dist = distance_to_line(line, c);
        c.dist = dist;
        mindist = min(c.dist, mindist);
        ans.push_back(c);
    }

    for (int i=0; i<ans.size();i++){
      //cout << ans[i].name << " " << mindist << " " << ans[i].dist << " " << endl;
      if(ans[i].dist == mindist){
        cout << ans[i].name << " ";
      }
    }

    ans.clear();
    cout << endl;
    cout.flush();

  }
}
