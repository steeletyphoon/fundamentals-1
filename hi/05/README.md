## A Colorful Salutation

```python
#!/usr/bin/env python3

import colors as c

print(c.clear)
print(c.yellow + "Hi, what's your name?")
name = input(c.orange + '--> ')
print(c.yellow + 'Well ' + name + ', nice to meet you.')

```

Time to color things up now that the base program is working. We'll add
a new special 'color' that isn't really a color at all. It clears the
screen when you print it like the other colors.

Notice that the last line is all yellow. Can you think of a way to make
