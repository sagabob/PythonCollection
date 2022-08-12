'''
Problem: https://leetcode.com/problems/ugly-number/
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

'''


def isUgly(num: int) -> bool:
    if num == 0:
        return False

    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1
