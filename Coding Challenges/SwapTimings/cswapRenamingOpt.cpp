#include <iostream>
#include <fcntl.h>
#include <string>
#include <map>
#include <fstream>
#include <vector>
#include <glob.h>
#include <stdio.h>
#include <linux/fs.h>
#include <sys/syscall.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
#define flags (RENAME_EXCHANGE)

void swap(const char* a, const char* b){
    syscall(SYS_renameat2, open(a,O_PATH), a, open(b,O_PATH), b, flags);
}

void getFiles(string target){
    if (target.empty()){
        cout << "Error: Directory not found" << endl;
        return;
    }
    map<string, string> dict;
    vector < string > arr;
    glob_t glob_result;
    glob(target.c_str(),GLOB_TILDE,NULL,&glob_result);
    for(unsigned int i=0; i<glob_result.gl_pathc; ++i){
      ifstream f(glob_result.gl_pathv[i]);
      arr.push_back(glob_result.gl_pathv[i]);
    }
    int i = 0;
    int j = arr.size()-1;
    while (i < j){
        swap(arr[i].c_str(),arr[j].c_str());
        i++;
        j--;
    }
}

//compile  with gcc swap.cpp -lstdc++fs
int main(int argc, char const *argv[]){
    string directory = "/home/bklo/Github/Daily-Programmer/Coding Challenges/SwapTimings/Test/*";
    double time0 = omp_get_wtime();
    getFiles(directory);
    double time1 = omp_get_wtime();
    printf("%10.2lf\n", 1000.*(time1-time0));
    return 0;
}
