class Solution {
public:
    bool isGoodArray(vector<int>& nums) {
        auto gcd = nums[0];
        for(auto n : nums) {
            gcd = __gcd(gcd, n);
        }

        return gcd == 1;
    }
};

// TC: O(n)
// SC: O(n)

/* 
Explanation:

ax + by = 1 if and only if, gcd(a,b) = 1
Initially assume gcd = nums[0]
Then go over each number n in nums and find gcd of gcd and n
Eg: [12, 5, 7, 23]
gcd = 12
gcd = gcd(12, 12) = 12
gcd = gcd(12, 5) = 1
gcd = gcd(1, 7) = 1
gcd = gcd(1, 23) = 1

thus, gcd = 1 of the entire array so there must be random two integers in the array for whom the equation ax + by=1 is true
*/