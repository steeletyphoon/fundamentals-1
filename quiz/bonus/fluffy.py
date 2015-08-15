"""The pink fluffy unicorn quiz questions module"""

import colors as c
from cli import ask

intro = c.magenta + '''
Welcome to the Pink Fluffy Unicorns quiz.
Let's test you knowledge...
''' + c.reset

def q1():
    answer = ask("What color are the unicorns?")
    if answer == "pink":
        print("And what a lovely color it is.")
        return True
    print("That is incorrect.")
    return False

def q2():
    answer = ask("What are the unicorns dancing on?")
    if answer.startswith("rainbow"):
        print("But isn't that physically impossible? Oh well.")
        return True
    print("Nope")
    return False

def q3():
    answer = ask("Use one word to describe the texture of their magical fur?")
    if answer.startswith("smile"):
        print(":)")
        return True
    print(":<")A
    return False

questions = [q1,q2,q3]
