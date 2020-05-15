#!/usr/bin/python
import os
import sys

if (sys.argv[1] == 'small'):
    os.system("python ./lib/small.py")

elif (sys.argv[1] == 'medium'):
    os.system("python ./lib/medium.py")

elif (sys.argv[1] == 'large'):
    os.system("python ./lib/large.py")

elif (sys.argv[1] == 'custom'):
    os.system("python ./lib/custom.py")


elif (sys.argv[1] == 'run-test'):
    if len(sys.argv) == 3:
        os.system("python ./test/algoritmos.py " + sys.argv[2])
    else:
        print('\033[91m' + '\nError: ' + '\033[0m' + ' run-test requires an Int argument. \n\ttry: py main.py run-test 100 \n')


elif (sys.argv[1] == 'help'):
    print('\033[94m' + '\n---  THE ANIMAL SHOW CLI ---\n' + '\033[0m')
    print("Usage:  python main.py [command] \n ")
    print("Commands:")
    print(
        "  run-test [int]: \t  performance tests and comparisons; with complexities N, NlogN, NxN\n")
    print("  small: \t \t  example with a small data instance  n=6, m=3 ,k=2")
    print("  medium: \t \t  example with a medium data instance n=9, m=4 ,k=3")
    print("  large: \t \t  example with a large data instance  n=20, m=6 ,k=10\n")
    print("  custom: \t \t  example with a custom data instance n=?, m=? ,k=?")
    print("  \t \t  \t * in the case of custom, modify the custom.py in the path ./lib/custom.py \n")


else:
    print(
        '\033[91m' + '\nError: ' + '\033[0m' + sys.argv[1] + ' is not a The Animal Show command. \n')
