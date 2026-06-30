class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        ret = 0
        i=0
        while i < len(s):
            if i+1 < len(s) and m[s[i+1]] > m[s[i]]:
                ret += m[s[i+1]] - m[s[i]]
                i += 1
            else:
                ret += m[s[i]]
            i += 1
        
        return ret
        # TC: O(1), SC: O(1)