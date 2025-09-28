class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums.size(); i++) {
            if(map.find(nums[i]) != map.end()) {
                map[nums[i]] += 1;
            }
            else {
                map[nums[i]] = 1;
            }
        }

        if(map.size() == nums.size()) {
            return false;
        }

        return true;
    }
};