#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;
int n;

class Cat {
public:
    string name;
    int order, level;


};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);

    int op, level;
    string name;
    cin >> n;
    for (int i=0; i<n;i++){
        cin >> op;
        if(op == 0 || op == 1){
            cin >> name >> level;
            //(op == 0) ? op1 : op2;
            // add element to heap and dictionary
        } else if (op == 2) {
            cin >> name;
            // update value of dictionary
        } else {
            // Print top of queue
        }
    }

    return 0;
}
