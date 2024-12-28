import sys

string_to_reverse = sys.argv[1]

def reverse_words(s):
    output = ''
    left, right = 0, 0

    while right < len(s):
        if s[right] != ' ':
            right += 1
        else:
            output += s[left:right+1][::-1]
            right += 1
            left = right

    output += ' '
    output += s[left:right + 2][::-1]
    return output[1:]


print(reverse_words(string_to_reverse))