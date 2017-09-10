# initial statement
words = "It's thanksgiving day. It's also my birthday, too!"
print (words)

# finding the word position and replacement of day with month
print (words.find('day'))
print (words.replace('day', 'month'))


# printing min and max
x = [2, 3, 4, 5, 6, -1, 22, 9910010, 29230, -230]
print "this is the min number in the list", min(x)
print 'this is the max number in the list', max(x)


# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

oldlist = ["hello",2,54,-2,7,12,98,"world"]

print oldlist[0], oldlist[len(oldlist) - 1]

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x) / 2]
second_list = x[len(x) / 2:]
print "first part of list", first_list
print "second part of list", second_list
# insert the second part of the list to the beginning of the list
second_list.insert(0, first_list)
print second_list
