import time

print("welcome to my python quiz, in this game it will help you improve your skills and mayabe get me an internship for the future")

ur_name = input("to get started please enter your name\n")

print(f"Hello {ur_name}, I am going to give you a basic of what you should know about the game that i made. You will be giving a multiple choice quesetion A to D  with a point system")






  # the function "options" are the multiple choice with a 2d tuple 
options = (
    ("A. Local Scope", "B. Global Scope", "C. Module Scope", "D. Block Scope"),
    ("A. \\i ", "B. \\f", "C. \\n", "D. \\d"), 
    ("A.0", "B.1", "C.2", "D.3"),
    ("A.True", "B.False"),
    ("A. /", "B.%", "C.//", "D.*") 

           
)


# For this section I have the questions and the awnsers dictionary with a for loop. I put the questions as the index and the awnsers as the value so I can be more accurate to what else I could do.
questions_and_awnsers = {
        "what kind of scope is in a def function" : "A",
    "Which of these options give out a new line after the string?" : "C",
    "In any index, what number does it start with" : "A",
    "When a 'if' statement does meet there conditions, the 'else' statement can be executed" : "A",
    "which operator divides numbers and gives an integer as a result " : "C",
    "Wha"
}    




the_counter = 0
ur_point = 0





for questions in questions_and_awnsers:
    
    
    print("------------------------------------------------------------------------------------------------------")
    print(questions)
    for option in options[the_counter]:
        print(option)
    
    the_awnser = input("please pick a letters as shown for the choices\n").upper()
# For this "while" loop, I was able to make sure if the user has the correct awnser and input within the choices I presented to them
    while True:
        if the_awnser in ["A","B","C", "D"]:
            if the_awnser == questions_and_awnsers[questions]:
                print("correct")
                ur_point += 1
                break
            else:
                print("incorrect")
                print(f"the correct awnser is {questions_and_awnsers[questions]}")
                break

        else:
            print("the letter or number that you have enter doesnt match the choices that are displayed")
            time.sleep(1.5)
            the_awnser = input("Please enter a vaild choice").upper()
    
   

    the_counter += 1

total_points = ur_point / len(questions_and_awnsers)

# This show the results of the users and to see if they pass
if total_points >= 90:
    print("congrats you have gotten an A")
elif 90 > total_points >= 80:
    print("you've gotten a B")
elif 80 > total_points >=70:
    print("you've gotten a C")
else:
    print("your score is pretty low and you need to study more to acheive your dream")


print(f"your score is {total_points}")





        
       
        


