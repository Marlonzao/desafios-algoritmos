#!/usr/bin/env python

first, second, third = 0, 1, 1
result = 0

while third < (4*(10**6)):
    third = (first+second)         
    first, second = second, third

    if third%2 == 0:
        result += third

print result