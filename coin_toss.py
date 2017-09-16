import random

# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

# Sample output should be like the following:

# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you

def coin_toss(toss):
# define the starting values
    attempt = 1
    heads = 1
    tails = 1
    result = ""
    for x in range(1, toss):
        new_flip = random.randint(0,1)
        if new_flip == 1:
            heads += 1
            result = "Heads it is!"
            print "Attempt #", attempt, ": Throwing a coin, its...", result,"Got", heads, "heads(s) so far and", tails, "tail(s) so far"
        else:
            tails += 1
            result = "Tails it is!"
            print "Attempt #", attempt, ": Throwing a coin, its...", result,"Got", heads, "heads(s) so far and", tails, "tail(s) so far"
        attempt += 1
    print "ending the coin toss!"
coin_toss(5001)