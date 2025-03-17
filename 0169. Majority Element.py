# C++

"""class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans = 0;
        int val = 0;

        for (auto x : nums) {
            if(val == 0){
                ans = x;
            }

            if (ans == x){
                val ++;
            }
            else{
                val--;
            }
        }

        return ans;
    }
};"""