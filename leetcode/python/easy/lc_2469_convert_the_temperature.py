"""
LeetCode: 2469 - Convert the Temperature
Difficulty: easy
Pattern: Math

Idea:
- Return [celsius + 273.15, celsius * 1.80 + 32.00]

Complexity:
- Time: O(1)
- Space: O(1)

Pitfalls:
- Floating point precision issues, but LeetCode accepts answers within 10^-5 margin.
"""

from typing import List


def solve(celsius: float) -> List[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]
