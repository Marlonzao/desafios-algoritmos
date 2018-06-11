#!/usr/bin/env python

def divisable(x):
    return (((x % 3) == 0) or ((x % 5) == 0)) 

total = 0
for n in range(1000):
    if(divisable(n)):
        total += n

print total