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
        # Horizontal Scanning
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: # If not found or not found at position 1
                if prefix == "":
                    return ""
                prefix = prefix[:-1]
        
        return prefix
        # TC: O(nm), SC: O(1)
        
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
