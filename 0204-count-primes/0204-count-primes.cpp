class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2) {
            return 0; // 0 and 1 are not prime
        }

        vector<bool> nums(n, true); // creates a boolean vector of size n with true as value

        for(int i = 2; i <= sqrt(n); i++) {
            if(nums[i]) {
                for(int j = i*i; j < n; j += i) {
                    nums[j] = false;
                }
            }
        }

        int ret = 0;
        for(int i = 2; i < n; i++) {
            if(nums[i]) {
                ret++;
            }
        }

        return ret;
    }
};