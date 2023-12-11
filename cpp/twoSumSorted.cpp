#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        for (int lefti = 0; lefti < numbers.size(); lefti++){
            cout << lefti << endl;
            //Binary search values
            bool valFound = false;
            int searchVal = target - numbers[lefti];
            int leftB = lefti+1;
            int rightB = numbers.size()-1;
            
            while  (leftB <= rightB){
                int checkI = std::floor(leftB + (rightB-leftB)/2);
                if (numbers[checkI] == searchVal){
                    return {lefti+1, checkI+1};
                } if (numbers[checkI] > searchVal){
                    rightB = checkI - 1;
                } else {
                    leftB = checkI + 1;
                }
            }
        }
        return {};
    }
};

int main(){

    Solution solution = Solution();
    vector<int> nums = {2,7,11,15};
    vector<int> result = solution.twoSum(nums, 9);
    cout << result[0] << " "<< result[1] <<endl;
 
    return 0;
}