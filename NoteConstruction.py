import math
import os
import random
import re
import sys
import collections



#
# Complete the 'constructNote' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def constructNote(magazine, note):
    noteCount = collections.Counter(note)
    magCount = collections.Counter(magazine)

    for x, y in noteCount.items():
        if x not in magCount or (x in magCount and y > magCount[x]):
            return False

    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    magazine_count = int(input().strip())

    magazine = []

    for _ in range(magazine_count):
        magazine_item = input()
        magazine.append(magazine_item)

    note_count = int(input().strip())

    note = []

    for _ in range(note_count):
        note_item = input()
        note.append(note_item)

    result = constructNote(magazine, note)

    fptr.write(str(int(result)) + '\n')

    fptr.close()