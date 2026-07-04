class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Horizontal Scanning:
        Basically, take two words and find the common prefix among them. Then compare that prefix 
        with the next word and choose the common prefix from that
        Vertical scanning:
        Get the first character in the first word and compare it across all words. If common, then
        build the prefix, if not at any point or reaches end of word for any word, return the prefix.
        WRONG:
        Brute force would be to have two loops and check until when all the strings are matching
        by checking strs[j][i].
        The optimized way would be to sort the array first so we have the smallest word in the
        beginning since the common prefix can't be longer than that. 
        """
        # Vertical Scanning
        if len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            c = strs[0][i] # Get the letter in the first word in each iteration
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c: # If i == len(strs[j]), then i cant go for another iteration. If the letter is not c also, return the first word until i
                    return strs[0][:i]
        return strs[0] # If it reached here, first word is the prefix
        # TC: O(mn), SC: O(1)

        # # Horizontal Scanning
        # if len(strs) == 0:
        #     return ""

        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     while strs[i].find(prefix) != 0: # If not found or not found at position 1
        #         if prefix == "":
        #             return ""
        #         prefix = prefix[:-1]
        
        # return prefix
        # # TC: O(nm), SC: O(1)
        
        # # Brute Force - WRONG
        # strs.sort()
        # pref = ""
        # for i in range(len(strs)):
        #     for j in range(len(strs[0])):
        #         pref += strs[i][j]
        #         for k in range(len(strs)):
        #             if pref not in strs[k]:
        #                 return pref[:-1]
        #             if len(pref) == 0:
        #                 return ""
        # return pref
