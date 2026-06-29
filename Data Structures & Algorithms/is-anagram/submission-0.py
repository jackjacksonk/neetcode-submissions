class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Counter creates a hash map of character frequencies
        return Counter(s) == Counter(t)