# 17) How do you set a global variable inside a function?
#
# A) Yes, we can use a global variable in other functions by
# declaring it as global in each function that assigns to it:

globvar = 0

def set_globvar_to_one():
    global globvar
    globvar = 1

def print_globvar():
    print(globvar)

set_globvar_to_one()
print_globvar()