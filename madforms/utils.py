"""This my awesome utility kitchen sink. Don't judge me."""

import colors as c

def ask(question):
    print(c.yellow + question + c.reset)
    answer = input("> " + c.base3)
    answer = answer.lower().strip()
    print(c.reset,end="")
    return answer

if __name__ == '__main__':
    print(c.clear)
    name = ask("What is your name?")
