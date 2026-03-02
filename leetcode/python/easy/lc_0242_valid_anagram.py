"""
LeetCode: 242 - Valid Anagram
Difficulty: easy
Pattern: Hash Counting

Idea:
- If lengths differ, it's impossible.
- Count characters in s and t and compare counts.

Complexity:
- Time: O(n)
- Space: O(k) where k is the alphabet size / unique chars

Pitfalls:
- Different lengths
- Unicode vs lowercase-only assumptions
"""

from collections import Counter


def solve(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)