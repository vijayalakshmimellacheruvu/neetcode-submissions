class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Stores the longest common prefix found so far
        res = ""
        # Iterate through each character index of the first string
        for i in range(len(strs[0])):
            # Check whether the character at index i matches in every string
            for s in strs:
            # If we reach the end of a string or find a mismatch,
            # the common prefix ends here, so return the result
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # If all strings have the same character at index i,
            # add that character to the common prefix
            res += strs[0][i]
        # If the entire first string matches every other string,
        # return the complete common prefix found
        return res