class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        count = [0]*26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch)-ord('a')] -= 1
        return all(c==0 for c in count)  # slightly more optimized instead of using a hashmap if we know its just lowercase english characters
        