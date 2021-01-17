#include <iostream>
#include <vector>

using namespace std;
int t, n;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(0);

  cin >> t;
  while(t--){
      cin >> n;
      vector<int> vals(n, 0);
      int sum;
      for(int i=0;i<n;i++){
          cin >> vals[i];
          cout << vals[i];
          if (vals.size()%2==0){
              sum += (vals[vals.size()/2 -1] + vals[vals.size()/2])/2;
          } else {
              sum += (vals[vals.size()/2]);
          }
      }
      cout << "\n" <<sum << endl;
      vals.clear();

  }
}
