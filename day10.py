#!/bin/python3

import sys

n = int(input().strip())

longest_one_count = 0;
current_one_count = 0

while n > 0:
    remainder = n % 2
    n = n // 2
    if remainder == 1:
        current_one_count += 1;
    else:
        current_one_count = 0;
    
    if longest_one_count < current_one_count:
        longest_one_count = current_one_count
    
    
print(longest_one_count)