#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int n, m;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    while(n!=0){
        vector<vector<int> > adj(n, vector<int>(n));
        for (int i=0;i<n;i++){
            for(int h=0;h<n;h++){
                cin >> adj[i][h];
            }
        }
        cin >> m;
        if (m==0){
            cout << 0 << " " << 0 << endl;
            cin >> n;
            continue;
        }

        vector<vector<int> > min_dp(m+1, vector<int>(n,9999999));
        vector<vector<int> > max_dp(m+1, vector<int>(n,0));
        for(int i=0;i<n;i++){
            min_dp[0][i] = 0;
            max_dp[0][i] = 0;
        }
        for (int turn=1;turn<m+1;turn++){
            for(int r=0;r<n;r++){
                if(turn==1){
                    min_dp[1][r] = adj[0][r];
                    max_dp[1][r] = adj[0][r];
                } else {
                    for(int r2=0;r2<n;r2++){
                        max_dp[turn][r] = max(max_dp[turn][r], max_dp[turn-1][r2] + adj[r2][r]);
                        min_dp[turn][r] = min(min_dp[turn][r], min_dp[turn-1][r2] + adj[r2][r]);
                    }
                }
            }
        }
        int best_max=max_dp[m][0];
        int best_min=min_dp[m][0];
        for (int r=0;r<n;r++){
            best_max=max(best_max, max_dp[m][r]);
            best_min=min(best_min, min_dp[m][r]);
        }
        cout << best_max << " " << best_min << endl;
        cin >> n;
        min_dp.clear();
        max_dp.clear();
        adj.clear();
    }
    return 0;
}
