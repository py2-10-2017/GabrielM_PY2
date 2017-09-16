import random



# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def score_grade(trys):
    print "Scores and Grades"
    for x in range(0, trys):
        random_grade = random.randint(60,101)
        if random_grade >=60 and random_grade <= 69:
             print "Your score was", random_grade, "That results in a D"
        elif random_grade >=70 and random_grade <= 79:
             print "Your score was", random_grade, "That results in a C"
        elif random_grade >= 80 and random_grade <= 89: 
             print "Your score was", random_grade,  "That results in a B"
        elif random_grade >= 90 and random_grade <= 100:
             print "Your score was", random_grade,  "That results in an A"
    print "end of the semester!"

score_grade(10)




