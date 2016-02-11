#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <iomanip>
using namespace std;

int main(){
    int n_degree;
    long double pi = 4,
          sum = 0,
          answer;
    cout << "How many digits of pi do you want to print? (Limit 100)" << endl;
    cin >> n_degree;
    if (n_degree > 100){
        cout << "Please selected a number under 50" << endl;
    }
    for (int i = 0; i <= 10000; i++){
        sum += pow(-1.0,i)/(2.0*i + 1.0);
    }
    answer = pi*sum;
    cout << "Here is the output of pi" << endl;
    cout <<  setprecision(n_degree) << answer << endl;
}
