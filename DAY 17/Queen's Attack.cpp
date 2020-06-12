#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the queensAttack function below.
int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {
int u= n-r_q;
int b= r_q-1;
int l= c_q-1;
int r= n-c_q;
int ru= min(r,u);
int lb= min(l,b);
int lu= min(l,u);
int rb= min(r,b);

for(int i=0;i<k;i++){
int p=obstacles[i][0];
int q=obstacles[i][1];



if(p>r_q && q==c_q)
{if(u==0)
continue;

u=min(u,p-r_q-1);
}

else if(p<r_q && q==c_q)
{if(b==0)
continue;

b=min(b,r_q-p-1);
}

else if(p==r_q && q<c_q)
{if(l==0)
continue;

l=min(l,c_q-q-1);
}

else if(q>c_q && p==r_q){
if(r==0)
continue;

r=min(r,q-c_q-1);
}



else if(p>r_q && q>c_q && p-r_q==q-c_q){
if(ru==0)
continue;

int ans=min(p-r_q,q-c_q);
ru=min(ru,ans-1);

}

else if(p<r_q && q<c_q && r_q-p==c_q-q){
if(lb==0)
continue;

int ans=min(r_q-p,c_q-q);
lb=min(lb,ans-1);

}

else if(p>r_q && q<c_q && p-r_q==c_q-q){
if(lu==0)
continue;

int ans=min(p-r_q,c_q-q);
lu=min(lu,ans-1);

}


else if(p<r_q && q>c_q && r_q-p==q-c_q){
if(rb==0)
continue;

int ans=min(r_q-p,q-c_q);
rb=min(rb,ans-1);

}


}

int sol=u+b+l+r+ru+lb+lu+rb;
return sol;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nk_temp;
    getline(cin, nk_temp);

    vector<string> nk = split_string(nk_temp);

    int n = stoi(nk[0]);

    int k = stoi(nk[1]);

    string r_qC_q_temp;
    getline(cin, r_qC_q_temp);

    vector<string> r_qC_q = split_string(r_qC_q_temp);

    int r_q = stoi(r_qC_q[0]);

    int c_q = stoi(r_qC_q[1]);

    vector<vector<int>> obstacles(k);
    for (int i = 0; i < k; i++) {
        obstacles[i].resize(2);

        for (int j = 0; j < 2; j++) {
            cin >> obstacles[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = queensAttack(n, k, r_q, c_q, obstacles);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

