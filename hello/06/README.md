# Hello World

![SkilStak Hello](http://skilstak.github.io/images/skilstak-terminal.png)

*Hello world* is a famous program written by millions. It's a great way
to start.

## Vim Editor Basics

A *character* is a letter, number, symbol or space that you can type.

A *text file* is a file with letters, numbers, spaces and other characters
in it.

An *editor* is a app used to change stuff in a file, for example, to create
a new `hello` program or edit a `server.properties` file to change
a Minecraft world to super flat.

A *screen-oriented editor* is an editor that doesn't need a mouse to
use. Since we are writing all our programs from a *Linux terminal* (like
other professional programmers) we will use *vi* (or *vim*) a famous
*screen-oriented editor* used by exceptional programmers since before
the Internet was invented. *vi* is on every UNIX/Linux computer there is.
This makes it a very useful tool to learn.

Here are the vi survival essentials you need to master at this point. You
will learn many more as you grow into this powerful editor:

* `i` - switch to INSERT mode (look in bottom left)
* `<arrows>` - move around in INSERT mode
* `<esc>` - switch to COMMAND mode from INSERT
* `<esc>u` - undo, which you can repeat
* `ZZ` - save and exit
* `ZQ` or `:q!` - just quit without saving
* `:w` - save without exiting

The secret is the arrows. Eventually you will use `INSERT` mode less and
less.

- [x] Concept: Screen-Oriented Text Editors<br>
- [x] Command: `vi`, `vim`, `view`

## hello1

```python
print('Hello world!')
```

Let's start with the simplest form. Create a new file with `vi hello`
and put just one line in it. Close the file and save it (`<esc>ZZ`)
and then run it simply with `python3 hello`.

This program has two basic parts: a `print()` *function* and a `'Hello
world!'` *string*.

A *function*, which gets its name from Algebra, is like a machine that takes
in something, does something, and optionally gives back or *returns*
something new. A vending machine is like a function. You put in something,
money and a button press, then the machine does something inside and
finally it gives you something in return. In this case `print()`'s only job
is to print something to the screen. The stuff you put into the function has
a fancy math-ish name as well *parameters*. The *parameter* to `print()` is
just `'Hello world!'`, which is itself a *string*.

A *string* is a combination of *characters*, letters, numbers, spaces
and punctuation strung together in a line as if they were beads on a
bracelet or necklace and tied at both ends with knots. The knots are
*quotes*, single (`'`) or double (`"`). If you leave off a knot then the
beads fall off. `'Hello world!'` is a *string* that is *passed* to the
`print()` *function*. There you are talking like a programmer already!

- [x] Concept: Functions
- [x] Function: `print()`
- [x] Concept: Strings
- [x] Command: `python3`

## hello2

```python
#!/usr/bin/python3

print('Hello world!')
```

The best programmers live by the mantra *Don't Repeat Yourself* or *DRY*
— even code-muggles can appreciate that. We have decided repeatedly
typing out `python3` is far too much work.  We just want to type `hello`
but how?

First, we have to tell the computer we want to be able to run the
file. We do this by changing the permissions of the file exiting the
file and typing `chmod +x hello` on the command line. This makes the `hello`
file runnable. Type `ll hello`. If you forget this command come back to
this document or type `h` on the command line to get help as a quick reference.
(Permissions are covered in [Raspi-1][] and [Shell-1][] courses.)

Next, we have to tell the computer which program we want to use to run our
Python `hello` script. By adding the executable permission we signaled to
the computer to look at the first line of our script for a shebang line.
This special line starts with a *hashtag* `#` and the *bang* is for the
exclamation point `!`. (Coders have all kinds of slang for different
characters.) We then add the full path to the program we want to run the
rest of the file. We'll use `which python3` from the command line to see
that `python` is actually `/usr/bin/python3` aha! Now let's run it to test
by just typing `hello` from the command line.

- [x] Concept: DRY
- [x] Concept: File System Permissions
- [x] Command: `chmod`
- [x] Command: `ls`, `ll`
- [x] Command: `h`
- [x] Concept: Shebang Line
- [x] Concept: Coder Slang
- [x] Command: `which`
- [x] Command: `type`
- [x] Concept: File System Paths

[Raspi-1]: http://github.com/skilstak/raspi-0
[Shell-1]: http://github.com/skilstak/shell-1


## hello3

```python
#!/usr/bin/python3

print('\033[0;33mhello world')
```

Now let's add some color. On a machine such at Linux with terminals
that support colors we can use special codes to make all the characters
that come after the code appear in a color. You can see these by typing
`colors` from the command line:

```
base03  #002B36 \033[1;30m
base02  #073642 \033[0;30m
base01  #586E75 \033[1;32m
base00  #657B83 \033[1;33m
base0   #839496 \033[1;34m
base1   #93A1A1 \033[1;36m
base2   #EEE8D5 \033[0;37m
base3   #FDF6E3 \033[1;37m
yellow  #B58900 \033[0;33m
orange  #CB4B16 \033[1;31m
red     #DC322F \033[0;31m
magenta #D33682 \033[0;35m
violet  #6C71C4 \033[1;35m
blue    #268BD2 \033[0;34m
cyan    #2AA198 \033[0;36m
green   #859900 \033[0;32m
reset   ------- \033[0m
clear   ------- \033[H\033[2J
```

This color selection we are using is called [Solarized Dark][]
and has origins in the science of being able to see everything
well.  [If you are a teacher or am ambitious student who does
not have these colors set up in your terminal you can look at
[`bin/solarized*`](http://github.com/skilstak/bin) for some help.]

You can cut and paste these using Linux terminal by simply selecting the
part you want to copy. (No need to 'cut' or 'copy' it. It automatically
copies it.) Then when you open your code you can paste the code by
entering insert mode with `i` and right-clicking. Put the code inside
of the string quotes.

***Don't spend time copying all the colors. You only need a couple
for now.***

One of the main goals of this part of this simple project is getting
familiar with really the only time you use your mouse on a Linux
command-line, to copy and paste text from other applications like a
web browser.

After you have pasted a color code like below run your program. What's the
color?

- [x] Concept: ANSI Color Codes
- [x] Concept: Solarized Color Palette
- [x] Concept: Linux Cut and Paste with Mouse
- [x] Command: `colors`

[Solarized Dark]: http://ethanschoonover.com/solarized

## hello4

```python
#!/usr/bin/python3

print('\033[0;33m' + 'hello world')
```

Obviously there has to be a better way to handle that complicated
code.  First let's give the color code its own string. We can join
the strings back together with the `+` *operator*. An *operator* is
one or symbols together that do something to the things around them
called *operands*. For `1 + 2` the `+` is the *operator* and the `1`
and `2` are *operands*. When used with strings the plus sign attaches
them to one another. Later we'll see how the same *operator* (ex: `+`)
can do different things depending on the type of *operands* (ex: string
or number).

- [x] Concept: Operators, Operands
- [x] Operator: `+`

## hello5

```python
#!/usr/bin/python3

yellow  = '\033[0;33m'

print(yellow + 'Hello world!')
```

I don't know about you but I would never remember the color for yellow if
I had to retype it so let's make a way to use the word `yellow` in place
of the `'\033[0;33m'`. We'll use a *variable*, sometimes called a *var*
for short. *Variables* are like boxes that can only contain one thing at
a time. You put things inside these variable boxes by assigning things
to them with the equals sign `=`, which is another *operator*. Equals
does not mean equals in this case. You would say `yellow` is *assigned*
the color code `'\033[0;33m'`. The thing on the right goes into the
thing on the left.

Once assigned we can use `yellow` anywhere we would type out that code.
Because the variable `yellow` never really changes we could call it a
*constant* which is exactly like a *variable* but never changes once
it is assigned a value the first time. In Python there really are not
true *constants* because you can always change them, but we can treat
it as a *constant* by just not changing it. Sometimes constant names are
typed in all capital letters, so `YELLOW` instead of `yellow` but we'll
keep it easier to type with lowercase. We'll talk about another way to
remember you have a constant when doing the [`colors`](../colors) project.

- [x] Concept: Variables
- [x] Concept: Constants
- [x] Concept: Assignment
- [x] Operator: `=`

## hello6

```python
#!/usr/bin/python3

yellow  = '\033[0;33m'

print(yellow + 'Hello ' + 'world!')
```

Now let's get crazy and use two colors, wahoooo! You already know how
to split a string in half and rejoin them with the `+`. Let's split the
two words in preparation for adding two colors. Don't forget both new
strings need their own quotes.

Notice how running this code is no different from the code
before. Sometimes we run a test on something that we know should be the
same as before but just want to make sure nothing changed. This is called
*regression testing*.

Can you guess what comes next? Try to add another color without looking
at the next step. You should know everything you need by now to do it.

- [x] Concept: Regression Testing

## hello7

```python
#!/usr/bin/python3

yellow  = '\033[0;33m'
blue  = '\033[0;34m'

print(yellow + 'Hello ' + blue + 'world!')
```

There. That wasn't so hard. Stop here. You are done with `hello` but there's
one more trick about color we'll show you.

## hello8

```python
#!/usr/bin/python3

import colors as c

print(c.yellow + 'Hello ' + c.blue + 'world!')
```

Yep. You don't have to type them all in. We did it for you and put them
all into what's called a *module* (or *mod* for short). Mods are handy
ways to keep code around in an organized way that you want to reuse. We'll
be reusing colors a lot in this course. You can peek ahead at what the
[`colors.py`](http://github.com/skilstak/lib) mod looks like inside, but we
won't learn how to make mods of our own for a while. 

Maybe you noticed using `c.` in front of the colors instead of `colors.`
to tell Python you want to use the variable from `colors`. This is
called an *alias* and allows us to save on typing. It also allows any
possible duplicate names from blowing each other away, say if we had our
own `blue` as well as `c.blue`. The `c.blue` we say belongs to another
*namespace*. Keeping your names from killing one another is very important
as your code gets more and more complicated. Python is very good and
protecting us from accidental name collisions. Other languages (such as
JavaScript, shell, and C) are no so good at it.

Looks like we are done, right?

- [x] Concept: Modules
- [x] Concept: Namespaces
- [x] Statement: `import`

## hello9

```python
#!/usr/bin/env python3

import colors as c

print(c.yellow + 'Hello ' + c.blue + 'world!')

```

Wait!? What if I email this amazing program to my friend and his computer
has `python3` in a different place? Maybe `/usr/local/bin/python3`
instead. Well some smart people decided how to get around this.

Every time you login to the terminal command line you are actually
connecting to a program, kind of like when you are in Minecraft and
can send commands with `/` instead of chatting. A program that runs
interactively like that to handle your commands is called a *shell*. On
Linux (and Mac) that shell program is called *Bash*, `/bin/bash` to be
more precise (but don't bash it, it's awesome). That's right, all that
Minecraft has been helping you learn to program by teaching you about
the command line.

Just like `yellow` in your program the shell also has variables, (which we
talk about a lot in [Shell-1](http://github.com/skilstak/shell-1)). These
variables that control things about your login are called *environment
variables*. Normally the `/usr/bin/env` program is used to show all the
variables available to you on your command environment of the shell
you are in. You can try it and see all the environment variables on
your system by typing just `env`. But if you put something after the
`env` like `env python3` env will find that program and run it --
wherever it may live. This allows us to share our programs more easily
with others and has become a standard. Memorize this shebang line.

- [x] Concept: Command-Line Shell
- [x] Concept: Environment Variables
- [x] Command: `bash`
- [x] Command: `/usr/bin/env`

[[&larr; Back](../06) | [Continue &rarr;](../08)]
