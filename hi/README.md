# Hi

![SkilStak Hi](http://skilstak.github.io/images/skilstak-hi.png)

**Approximate Time:** 30 minutes

This program is a more personalized version of [hello](../hello) that
prompts the user for a name before saying hello. The goal of the
project is to learn how to prompt users for information that they type in,
which is a core part of any interactive command-line script including the
[eightball](../eightball) program we'll make later. It is also obviously
a core part of any sort of interactive story or text adventure game such as
the [storyeng](http://github.com/storyeng) games we will make in
[Python-1](http://github.com/skilstak/python-1) and 
[Python-2](http://github.com/skilstak/python-2).

## hi1

```python
#!/usr/bin/env python3

print("Hi, what's your name?")
```

First let's just do the same thing we did to begin [hello](../hello) by just
printing something out. In fact, you can just `cp hello hi` if you want to
save yourself the `chmod u+x hi` command since the proper permissions have
already been set on hello.

Notice that we use `"` instead of `'` because the `what's` already used
a `'` and it would mess it up. Python let's you use either `'` or `"`
for strings and they don't have different functions (as they do in some
other programming languages).

## hi2

```python
#!/usr/bin/env python3

print("Hi, what's your name?")
input('--> ')
```

Now let's get some input from the user. The `input()` function makes
our program wait for the user to type something in and press the
enter key. Whatever we pass to the function inside of the parentheses
(or *parens*) `()` will be printed to the screen to let the user know
to type something in. This is called a *prompt*. There's also a fancy
name for the stuff we pass into the parenthesis like coins in a soda
machine. *Parameters* is what computer scientists call them (the rest
of us say *params*).

## hi3

```python
#!/usr/bin/env python3

print("Hi, what's your name?")
name = input('--> ')
print(name)
```

Now we add a `name` variable that will have whatever the user typed
inside of it so we can use it later.  The `input()` function is like
a machine that spits something out. When a function does this we call
it *returning* a value. We store that returned value into `name` by
assigning it just like we did color codes in [hello](../hellow).

To make sure all this plumbing is working we are going to just print
the `name` variable. `print()` is universally used to test code so
we can see what is going on &mdash; especially when things get more
complicated. Often this is referred to as a *debug print statement*. There
are much fancier ways to debug, (which means to track down problems),
in code. But the old reliable `print()` statement is always there to
help us out. We'll delete it later once we know our code is working.

Using all our fancy new words for things we can describe `name =
input('-->')` as a line of code that calls the *function* `input()` and
passes a single *string* as a *param* for the *prompt* and *returns*
another *string* containing what the user typed into the `name`
*variable*. By now that sentence should make sense enough to not sound
like some coder-geek foreign language. Yes, face the reality, YOU are
becoming a geek. Just own it and start imagining how you will soon use
your new superpower for good. Oh, and don't forget to go outside once
in a while.

## hi4

```python
#!/usr/bin/env python3

print("Hi, what's your name?")
name = input('--> ')
print('Nice to meet you, ' + name + '!')
```

Now let's do something more useful with the `name` variable. Don't forget
the space after the word *you* **inside of the string** because that will
keep the name from being too close.

## hi5

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

## hi6

```python
#!/usr/bin/env python3

import colors as c

print(c.clear + c.yellow + "Hi, what's your name?")
name = input(c.orange + '--> ')
print(c.yellow + 'Well ' + name + ', nice to meet you.')
```
Now, can you figure out how to make the `-->` prompt a different color than
what the user types in? Give it a try before you proceed.

## hi7

```python
#!/usr/bin/env python3

import colors as c

print(c.clear + c.yellow + "Hi, what's your name?" + c.reset)
name = input('--> ' + c.orange)
print(c.red + 'Well ' + c.magenta + name + c.red + ', nice to meet you.')
```

Great job! You have completed `hi`. And by the way you can use `c.pink`
instead of `c.magenta` if it is easier to remember. Same with `c.purple`
and `c.violet`.
