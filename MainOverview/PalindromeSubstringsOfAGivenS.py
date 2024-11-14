
from typing import List

def countPalindromeSubStrings(s: str) -> int: # Runtime O(n), O(1) space
    result = 0

    for pos in range(0, len(s)):
        l,r = pos, pos
        # Look for odd palindromic strings, middle is center char
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            result += 1
            l-= 1
            r+= 1
        
        # Look for even palindromic strings, middle is between chars
        l,r = pos, pos +1
        while(l >=0 and r < len(s) and s[l] == s[r]):
            result += 1
            l-= 1
            r+=1
            
    return result