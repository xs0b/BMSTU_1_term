#include <iostream>
#include <vector>
using namespace std;

int min_mas(vector<int> mas){
    int i_min = 0;
    int min_now = mas[0];
    for (int i = 1; i < mas.size(); ++i){
        if (mas[i] < min_now){
            min_now = mas[i];
            i_min = i;
        }
    }
    return i_min;
}

int main(){
    int n;
    cin >> n;
    int r = n;
    int c = n;
    int i_min = 0;
    int t;
    vector<vector<int> > arr(r, vector <int> (c));
    for (int i = 0; i < r; ++i){
        for (int j = 0; j < c; ++j)
            cin >> arr[i][j];
    }

    for (int i = 0; i < r; ++i){
        i_min = min_mas(arr[i]);
        t = arr[i][i_min];
        arr[i][i_min] = arr[i][i];
        arr[i][i] = t;
    }
    return 0;
}



