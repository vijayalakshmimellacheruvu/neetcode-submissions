from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # by using sort we get t.c as O(m.nlogn)
        # using hashmap-by counting the characters and compare them - O(m.n.26)-O(m.n)
        # initializing a hashmap
        res = defaultdict(list)
        for s in strs:
            #counting each character in each string
            count = [0] * 26
        #traversing every single character through each string
            for c in s:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())
    
