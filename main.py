"""This programs includes a code which allow to check if the user input match with certains condition, the conditions are exposed bellow"""



# The primary condition
"""If user_input % 4 != 0, user_output = False""" # The test stop here, it doesn't match with the first condition that is crucial for the next one. # result = user_output = False

# First Part of the condition, We evalute if the number is a multiple of 4, 100, and 400
"""If user_input % 400 == 0, user_output = True""" # If the year enter into this condition, it should be that the year is superior to 400 or equivalent to 400 

# Second part of the condition, We evalute if the number is a multiple of 4, but not of 400, and not of 100
"""If user_input % 4 == 0 and not user_input % 100 == 0""" # If the year enter into this condition, it should be that the year is inferior to 400 and not a multiple of 100





# Logic of the code

def check_bissextile(user_input):
    if user_input % 400 == 0 or (user_input % 4 ==0 and not user_input % 100 == 0):
        print("L'année est bissextile")
        user_output = True
    else:
        print("L'année n'est pas bissextile")
        user_output = False


def conversion(user_input):
    try:
        user_input = int(user_input)
        if user_input > 0:
            check_bissextile(user_input)
        else:
            select_years()
    except:
        select_years()


def select_years():
    user_input = input("Veuillez saisir une année ")
    conversion(user_input)


select_years()
