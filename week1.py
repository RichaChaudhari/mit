""" Problem 1
10/10 points (graded)

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:"""
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
    else:
        count += 0
print('Number of vowels: ' + str(count))


#problem 2
"""Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2"""

count = 0
for letter in range(len(s)-2):
    if s[letter] == 'b' and s[letter+1] == 'o' and s[letter+2] == 'b':
        count += 1
    else:
        count += 0
print('Number of times bob occurs is: ' + str(count))


#problem 3
"""Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc"""
emp = ""
d = {}
count = 0
for letters in range(len(s)):
    if letters < len(s)-1:
        if s[letters] <= s[letters+1]:
            emp = emp + s[letters] 
            count += 1
        elif s[letters] > s[letters+1] and s[letters- 1] <= s[letters]:
            emp = emp + s[letters]
            count +=1
            d[emp] = count
            emp = ""
            count = 0
        else:
            ans = len(emp)
            d[emp] = count
            count = 0
            emp = ""
    else:
        if s[letters] >= s[letters-1]:
            emp = emp + s[letters]
            count += 1
            d[emp] = count
import operator
keyMax = max(d.items(), key = operator.itemgetter(1))[0]
print('Longest substring in alphabetical order is: ' + keyMax)