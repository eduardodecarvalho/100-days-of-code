'''
Given a string s, return the maximum length of a 
substring
 such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
'''


def maximumLengthSubstring(s):
    left, right = 0, 0
    _max = 1
    counter = {}

    counter[s[0]] = 1

    while right < len(s) - 1:
        right += 1
        if counter.get(s[right]):
            counter[s[right]] += 1
        else:
            counter[s[right]] = 1

        while counter[s[right]] == 3:
            counter[s[left]] -= 1
            left += 1
        _max = max(_max, right - left + 1)

    return _max


print(maximumLengthSubstring("bcbbbcba"))
print(maximumLengthSubstring("aaaa"))
