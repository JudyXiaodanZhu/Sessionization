# Approach
My approach to this question is that considering the runtime, using a dictionary in python is the fastest data structure, comparing to lists, heaps and trees. Moreover, since we need to constantly check if the user session has expired, searching is faster for dictinaries. Perhaps one improvement if this scales is that after all the session have ended and all outputs need to be printed, I tried to find the line with the earliest input time by search through the dictionary. I should have first put everything in a heap and then just pop the heap. That should reach a better space complexity.

# Environment
1. python 3.6
2. import sys, csv, datetime

# Run
Run the run.sh file
