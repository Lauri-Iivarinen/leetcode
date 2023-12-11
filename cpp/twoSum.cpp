#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        //int leftI = 0;
        for (int leftI = 0; leftI < nums.size(); leftI++){
            for (int i = leftI+1; i<nums.size(); i++){
                if (nums[leftI]+nums[i] == target){
                    std::vector<int> result = {leftI, i};
                    return result;
                }
            }
        }

        return {};
    }
};

int main(){
    vector<int> target = {4,7,11,15,2};
    Solution solution = Solution();
    vector<int> result = solution.twoSum(target, 9);
    //Convert to string
    cout << "Hohoo" << result[0] << result[1] << endl;
    return 0;
};