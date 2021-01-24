#include <iostream>
#include <deque>

using namespace std;
int t, n;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    for (int i=0;i<t;i++){
        cin >> n;
        deque<int> order;
        order.push_back(n);
        int back;
        for(int j=n-1;j>0;j--){
            order.push_front(j);
            for(int k=j;k>0;k--){
                back = order.back();
                order.pop_back();
                order.push_front(back);
            }
        }
        for(int i=0;i<n;i++){
            back = order.front();
            order.pop_front();
            cout << back << " ";
        }
        cout << endl;

    }

}
