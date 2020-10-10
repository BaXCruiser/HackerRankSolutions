#include <bits/stdc++.h>
//BaXCruiser

using namespace std;
vector<string> split_string(string);

int solve(int n, vector<int> coins) {
    int c=0;
    for (int i=0;i<=coins[3];i++)
    { if (i*10>=n)
        {if(i*10==n)
          c++;
          break;}
        for (int j=0;j<=coins[2];j++)
        { if(i*10+j*5>=n)
            { if(i*10+j*5==n)
               c++;
               break;
             }
            for (int k=0;k<=coins[1];k++)
            { if(i*10+j*5+k*2>=n)
              { if (i*10+j*5+k*2==n)
                c++;
                break;}
              if (n-(i*10+j*5+k*2)<=coins[0])
                c++;
            }
        }
    }
    return (c);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string coins_temp_temp;
        getline(cin, coins_temp_temp);

        vector<string> coins_temp = split_string(coins_temp_temp);

        vector<int> coins(4);

        for (int coins_itr = 0; coins_itr < 4; coins_itr++) {
            int coins_item = stoi(coins_temp[coins_itr]);

            coins[coins_itr] = coins_item;
        }

        int result = solve(n, coins);

        fout << result << "\n";
    }

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
