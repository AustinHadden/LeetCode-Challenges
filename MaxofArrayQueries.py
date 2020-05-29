import math
import os
import random
import re
import sys



#
# Complete the 'maxArrayQueries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def maxArrayQueries(n, queries):
    arr = [0] * (n + 1)

    for x in queries:
        start = x[0] - 1
        end = x[1]
        k = x[2]
        # positive k values between start and end
        arr[start] += k
        # negative k values after end
        arr[end] -= k

    max_value = 0
    count = 0
    # add all values in array together keeping track of the max
    for i in arr:
        count += i
        if count > max_value:
            max_value = count

    return max_value

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = maxArrayQueries(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()