#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    res = " ".join(x.capitalize() for x in s.split(" "))
    print(res)


if __name__ == '__main__':

    s = input()
    solve(s)

