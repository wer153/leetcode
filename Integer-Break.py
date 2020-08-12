class Solution:
    def integerBreak(self, n: int) -> int:
        max_product = -1
        if n==2:
            return 1
        elif n==3:
            return 2
        for i in range(2, math.floor(n**0.5)+1):
            max_product = max(max_product, (i**((n//i)-1))*((n%i)+i))
        return max_product
   
"""

https://leetcode.com/problems/integer-break/
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

Accepted
110,214
Submissions
218,860
"""
   