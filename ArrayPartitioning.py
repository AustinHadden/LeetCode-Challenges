import math
import os
import random
import re
import sys
import collections



#
# Complete the 'partitionArray' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY numbers
#

def partitionArray(k, numbers):
    yes = "Yes"
    no = "No"
    
    if not k and numbers == 1:
        return yes

    num_len = len(numbers)
    
    if k > num_len or num_len % k:
        return no

    group_num = num_len // k
    cnt = collections.Counter(numbers)

    if group_num < max(cnt.values()):
        return no

    return yes

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = partitionArray(k, numbers)

    fptr.write(result + '\n')

    fptr.close()