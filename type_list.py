mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]


def identify_list(input_list):
    new_string = ''
    total = 0
    for id in input_list:
        if isinstance(id, int) or isinstance(id, float):
          total += id
        elif isinstance(id, str):
            new_string += id

    if new_string and total:
        print "This is a mixed typed"
        print "The string portion is: ", new_string
        print "The sum of value is: ", total

    elif new_string:
        print "What you entered is a string type"
        print new_string, " is what was entered"
    
    else:
        print "What you entered is a whole number or float"
        print total, " is the sum value"

print identify_list(mixed_list)
print identify_list(integer_list)
print identify_list(string_list)