"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730314515"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune_cookie : int = int(randint(1, 100))

if 0 < fortune_cookie < 30:
    print("A lifetime of happiness lies ahead of you.")
else: 
    if 30 < fortune_cookie < 60:
        print ("A pleasant surprise is waiting for you.")
    else:
        if 60 < fortune_cookie < 80:
            print("A faithful friend is a strong defense.")
        else:
            print("Adventure can be real happiness.")
       
print("Now, go spread positive vibes!")