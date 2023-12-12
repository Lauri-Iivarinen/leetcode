/*
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/
#include<string>
#include<iostream>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        char prev = 'A';
        for (int i = 0; i < s.size(); i++){
            if (s[i] == 'I'){
                num++;
            }else if (s[i] == 'V' && prev == 'I'){
                num += 3;
            } else if (s[i] == 'V'){
                num += 5;
            }else if (s[i] == 'X' && prev == 'I'){
                num += 8;
            } else if (s[i] == 'X'){
                num += 10;
            }else if (s[i] == 'L' && prev == 'X'){
                num += 30;
            }else if (s[i] == 'L'){
                num += 50;
            }else if (s[i] == 'C' && prev == 'X'){
                num += 80;
            }else if (s[i] == 'C'){
                num += 100;
            }else if (s[i] == 'D' && prev == 'C')
            {
                num += 300;
            }else if (s[i] == 'D')
            {
                num += 500;
            }else if (s[i] == 'M' && prev == 'C')
            {
                num += 800;
            }else if (s[i] == 'M')
            {
                num += 1000;
            }

            prev = s[i];
        }

        return num;
    }
};

int main(){

    Solution solution = Solution();

    int val1 = solution.romanToInt("III");
    int val2 = solution.romanToInt("IV");
    int val3 = solution.romanToInt("XIX");
    int val4 = solution.romanToInt("LVIII");
    int val5 = solution.romanToInt("MCMXCIV");

    cout << val1 << endl;
    cout << val2 << endl;
    cout << val3 << endl;
    cout << val4 << endl;
    cout << val5 << endl;

    return 0;
}
