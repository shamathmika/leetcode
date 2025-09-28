class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ret = 0;
        for(int i = nums.size() - 1; i >= 2; i--) {
            if(nums[i] < (nums[i-1] + nums[i-2])) {
                ret = max(ret, nums[i] + nums[i-1] + nums[i-2]);
            }
        }

        return ret;
    }
};

// TC: O(nlogn)
// SC: O(1)