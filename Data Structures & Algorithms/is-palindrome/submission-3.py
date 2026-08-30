import math


class Solution:

  def isPalindrome(self, s: str) -> bool:
    s = s.lower()

    # 1. Clean the string safely
    clean_s = ""
    for c in s:
      if c.isalnum():
        clean_s += c
    s = clean_s

    # 2. Extract halves
    first_half = s[0 : len(s) // 2]
    # Reverse the second half so it reads backwards
    second_half_reversed = s[math.ceil(len(s) / 2) : len(s)][::-1]

    # 3. Compare
    if first_half == second_half_reversed:
      return True
    return False