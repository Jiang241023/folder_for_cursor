from typing import Dict
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_TO_INTEGER: Dict[str, int] = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = ROMAN_TO_INTEGER[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if ROMAN_TO_INTEGER[s[i]] >= ROMAN_TO_INTEGER[s[i + 1]]:
                total += ROMAN_TO_INTEGER[s[i]]
            else:
                total -= ROMAN_TO_INTEGER[s[i]]
        return total
s1 = ["III", "LVIII", "MCMXCIV"]
roman_to_integer = Solution()
for s in s1:
    print(f"Roman: {s}, Integer: {roman_to_integer.romanToInt(s)}")
