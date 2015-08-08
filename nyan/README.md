# Infinite Looping Nyan Cat

[![Nyan, Nyan, Nyan](http://img.youtube.com/vi/wZZ7oFKsKzY/0.jpg)](https://youtu.be/wZZ7oFKsKzY)

**Approximate Time:** 45 minutes

Did you know *nyan* is the sound a Japanese cat makes? Sure you did. Well
before you create your new program file with `vi nyan` or `vi meow`
watch the [10 hour video for inspiration](https://youtu.be/wZZ7oFKsKzY),
or not.  Oh, and don't forget to `chmod u+x nyan` after you create it.

Truth is this project is just an excuse to learn how to create
loops that never end or *infinite* loops and how to stop them with
`<control>-c`. We'll also see what they can do to a machine with the
`top` command.

## nyan1

```python
#!/usr/bin/env python3

print('Nyan')
```

First we just print *nyan*. Make sure you don't forget the standard
shebang, which you should have memorized pretty much by this point. `chmod
u+x nyan` the file if you need to. Run it to make sure all is in order. It
is always a good idea to start with something crazy simple to make sure
you didn't miss something obvious.


## nyan2

```python
#!/usr/bin/env python3 

while True:
    print('Nyan')
```

Now for the *loop* part. If you have played any
[CodeCombat](http://codecombat.com) you will probably remember the
`loop:` thingy. Well forget it. There is no such thing in *actual*
Python code. The creators told me they decided to add it because it
was too much to introduce a *real* loop like the one we'll add below. I
think you'll agree it isn't that hard to understand.

There are three specific changes here to make the loop work:

1. The line `while True` was added (note the capital `T` in `true)
2. The colon (`:`) as added after `while True:`
3. The original `print('Nyan')` line was *indented* with *tab* (4 spaces)

The word `True` is capitalized because is special. It is called a
*boolean*, which is a fancy word for values that are `True` or `False`.

We also added the loop keyword `while` which must always be followed with
a condition. A condition is like a question with a true or false answer.
Computers only understand true or false, on or off, 1 or 0 when you
get right down to it. But this is an easy question for the computer to
answer. How often is `True` true? If you answered forrrreeeeevvvvvaaa
you get bonus points. So the next question is how long does `while True:`
loop? Yep, same answer. But *what* loops forever? That's the third change.

We added a colon `:` to the end of the `while True` line to show the
beginning of a *block* of code to come. Blocks are lines of code that go
together inside of other code, in this case, a loop. The lines of code
in the block don't run unless the condition of the loop is true, which is
forever in this case. The other part of a block is the four spaces before
`print('Nyan')`. This is the other part of a block in Python. Python
sees the `:` and then looks for all the lines that are *indented* that
follow it.

Indenting is when you put spaces or tabs in front of the line. In our
case we will use the tab key because VIM turns tabs into 4-spaces. You
usually never want actual tab characters in your code.

> Now is a good time to talk about one of Python's most controversial
> aspects, (which means something that coders argue about a lot). Python
> is a *whitespace significant* langauge. This means that unlike most every
> other language around when Python came out, the creators of Python decided
> to make Python see spaces and tabs as part of the *syntax*. Syntax is
> the stuff of the langauge, the details, the colons, the way you write it.
> This meant that if you forgot a space or put in too many spaces your code
> would not work. This infuriated most traditional programmers (including
> this author) and most swore an oath never to program in Python (usually
> preferring Perl, C, and PHP instead). More than a decade later the use of
> forced whitespace has proven a big win responsible for millions of lines
> of readable code while the whitespace freedom Perl and other languages
> allowed created millions of lines of 'spaghetti' and 'code that looked
> like a cat walked across your keyboard'. Python's strict, there is one
> best way to do it' (including the style of the code itself), won v.s. the
> artistic 'there is more than one way to do it' approaches of Perl and
> others. Whatever the reason in the end, Python has clearly dominated
> anywhere a lot of code is going to be written, read and maintained by
> a lot of different people. This also made Python hands-down the easiest
> language to learn because all the missed `{`s and `;`s were gone. The moral
> of the story? Python won, just don't forget to line up your lines.

## Stopping the Loop

Ok, so you have started your `nyan` program and *it isn't stopping!*
Keep calm and `<control>-c` (that's both keys at the same time). This
stops the program by sending it an *interrupt signal*, (which we'll
learn more about later). The `<control>` key is in the bottom left of
the keyboard. Practice typing the `<control>` key with your left pinky
and the `c` key your left pointer finger. You'll be doing this a lot.

## Loops Hurt Computer Brains

Here's something fun. Start up another terminal and login so you have
two terminals at once. In one of the terminals run the command `top`
and watch how the numbers change. Type `z` while running `top` to see it
all in pretty color. In the other terminal start your `nyan` program. See
anything change in your `top` terminal? ;) Remember to stop `nyan` just
type `<control>-c` and type `q` to stop the `top` terminal. If you panic
you can just close your terminal and everything should get stopped as
well. But learn how to cancel these things because every programmer ends
up having to interrupt stuff they are working on.

For a really demented friendly competition put on some theme 'ZZ Top'
music and see which of you in the class can make their loop faster than
the other and be #1 on the top list. (Did I really just encourage you to
slam the server CPU? Sigh, I'm a horrible teacher. But hey, any excuse
to play some 'ZZ Top'.)

## nyan3 

```python
#!/usr/bin/env python3 

while True:
    print('Nyan', end=' ')
```

Oh, and there is this cool thing in Python 3 where if you add `, end='
'` you can make the `Nyan`s print on the same line. This is because
every time you use `print('Nyan')` it actually adds something called
a *new line* character that you can't see.  (In fact you can actually
print extra new lines in your strings by adding `\n`.) When you add `,
end=' '` you make Python change the character is uses by default to end the
line. Now it prints a space or whatever you set `end` to at the end.

## nyan4

```python
#!/usr/bin/env python3 

import colors as c

while True:
    print(c.blue + 'Nyan', end=' ')
```

Annnnd now the colors of course. They are so aesthetically pleasing
(fancy words for pretty) with no logical value whatsoever. It just looks
cool. 

## nyan5

```python
#!/usr/bin/env python3 

import colors as c

while True:
    print(c.random_color() + 'Nyan', end=' ')
```

'Cuz `random_color()`. That is all.

## More ...

Can you get yours to pick a random color for every letter of the word
*Nyan*? Just fun stuff.

