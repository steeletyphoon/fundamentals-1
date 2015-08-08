# Ooooo, Pretty Colors

![Solarized Color Palette](http://ethanschoonover.com/solarized/img/solarized-palette.png)

Most classes would stop right here. But let's add some
color. Somehow programming is more fun with colors and these days
adding color to terminal programs is pretty easy. Most terminals
are still limited to 16 colors so we will use the [Solarized Dark
Theme](http://ethanschoonover.com/solarized), our favorite here at
SkilStak. What are the colors you ask? Type `colors` on the command-line
to see:


[If you are a teacher or am ambitious student who does not
have these colors set up in your terminal you can look at
[`tools`](../tools) for some help.]

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

[[&larr; Back](../03) | [Continue &rarr;](../04)]
