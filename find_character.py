# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# Here's an example:

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Copy
# Hint: how many loops will you need to complete this task?

def findchar(word_list, char):
    newlist = []
    for input in range(0, len(word_list)):
        
        if word_list[input].find(char) != -1:
            newlist.append(word_list[input])
            
    print newlist

word_list = ['hello','world','my','name','is','Anna']
findchar(word_list, 'o')
