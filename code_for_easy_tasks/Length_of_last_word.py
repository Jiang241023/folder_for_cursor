from typing import List, Dict
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
s1 = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
Length_of_Last_Word = Solution()
for s in s1:
    print(f"length of last word of '{s}': {Length_of_Last_Word.lengthOfLastWord(s)}")