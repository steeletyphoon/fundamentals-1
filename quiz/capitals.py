import colors as c
from utils import ask


intro = c.magenta + '''
Welcome to the capitals quiz.
''' + c.reset

def q1():
    answer = ask("What is the capital of North Carolina?")
    if answer == "durham":
        print("Nope, but close, literally")
        return False
    elif answer == "raleigh":
        print("YES!!")
        return True
    else:
        print("Nope.")
        return False 

def q2():
    answer = ask("What is the capital of Utah?")
    if 'salt lake' in answer:
        print("YES!!")
        return True
    else:
        print("Nope.")
        return False 

def q3():
    answer = ask("What is the capital of Assyria?")
    if answer == "assur":
        print("YES!!")
        return True
    else:
        print("Nope.")
        return False 

questions = [q1,q2,q3]

