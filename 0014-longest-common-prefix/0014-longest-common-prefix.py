class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return "null"

        prefix = strs[0]
        for word in strs[1:]:
            j = 0
            while j < len(prefix) and j < len(word) and prefix[j] == word[j]:
                j += 1
            prefix = prefix[:j]
            if not prefix:
                return ""
        return prefix
            
        