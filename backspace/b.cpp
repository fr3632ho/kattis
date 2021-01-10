#include <vector>
#include <iostream>
#include <string.h>
using namespace std;

string input;
int main(){
  cin >> input;
  char text[input.size()];
  char out[input.size()];


  strcpy(text, input.c_str());
  // for(int i=0;i<input.size();i++){
  //   cout << input[i];
  // }
  // cout << endl;

  int i=0, j=0;
  while(i<input.size()){
    char curr;
    curr = text[i];
    //cout << curr << "\n";
    if(curr == '<' && j>=0){
      j = max(j-1, 0);
      out[j] = ' ';
      //j = i-1;
    } else {
      out[j] = curr;
      j++;
    }
    i++;
  }

  if(j!=0){
    for(int k=0;k<input.size();k++){
      if(out[k] != ' ' && k < j) {
        cout << out[k];
      }
    }
    cout << endl;
  }
  cout.flush();
}
