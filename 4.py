#!/usr/bin/env python


def is_palindrome(num):
    num_str = str(num)
    num_len = len(num_str)
    for i in range(0, num_len):
        if num_str[i] != num_str[num_len - i - 1]:
            return False
    return True


def find_palindrome():
    palindromes = []
    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            mul = x * y
            if is_palindrome(mul) and mul not in palindromes:
                palindromes.append(mul)
    return palindromes


palindromes = find_palindrome()
palindromes.sort()
print(palindromes)
