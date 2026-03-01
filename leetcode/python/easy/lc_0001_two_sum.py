"""
LeetCode: 1 - two_sum
Difficulty: easy
Pattern: <Hash Map>

Idea:
- <Hash Map>

Complexity:
- Time: O(n)
- Space: O(n)

Pitfalls:
- <>
"""

from typing import List

def solve(nums: List[int], target: int) -> List[int]:
    seen = {} #valor -> indice
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []