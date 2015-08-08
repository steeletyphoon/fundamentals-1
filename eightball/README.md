# Magic Eight Ball

[![Don't Count on It](http://img.youtube.com/vi/mFOracFClBg/0.jpg)](https://youtu.be/mFOracFClBg)

**Approximate Time:** 90 minutes

The magic eight ball is a popular, sooth-saying toy predicting the
futures of kids, their pets, parents, and teachers for decades. The fun
part about the coded version we are going to make is that you can change
it up and even save off the conversations you have with it when asking
it lots of questions.

```
--> Should we make a magic eight ball?
It is decidedly so.
```

## eightball01

```python
#!/usr/bin/env python3

import colors as c

print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)
```

Let's just get something to print for now to make sure all the basics are
working. Don't forget to `cp` an existing program or `touch eightball;
chmod u+x eightball` to create a new `eightball` file for your that
can be run. You should already know all about [`colors`](../colors)
at this point so we'll go ahead and use them.

Here's something new, the triple-quote *long string*. A long string is,
um, a long string. You can use single quotes `'` or double `"` and
everything inside is included in the string. This includes all the line
returns and words with single and double quotes with them. That's right.
Everything you put in a triple quote just gets included like you want. We
use long-strings a lot for large amounts of text and ASCII art. In fact, you
can use a triple quote later when adding more answers if you want to 
get really creative and include ASCII art answers to your list.

## eightball02

```python
#!/usr/bin/env python3

import colors as c

print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = ['Yes.','No.','Maybe']
print(answers)
```

Now let's add some answers in a *list*. A *list* is a Python thing
that is exactly what it sounds like, just a list of items. The
items in the list can be anything you can put into a *variable*,
strings, numbers, other variables, even functions, (which we do in
[Python-1](http://github.com/skilstak/python-1)).

You tell Python you want to use a list with square brackets `[]`. Inside
the bracket you put the items of your list separated with commas `,`. You
can have a list on on one line or on more than one line. It really
depends on your items and how many you have. For now since we only have
a few answers, and they all fit on one screen, we'll use one line.

Add the `print(answers)` just to make sure everything is working. You'll
delete it later. This is called a *debug* `print` and is common for seeing
what your program is doing while you develop it.

## eightball03

```python
#!/usr/bin/env python3

import colors as c

print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    c.green + 'Yes.' + c.reset,
    c.red + 'No.' + c.reset,
    c.base01 + 'Maybe.' + c.reset
]

print(answers)
```

On second thought how about a little color for each answer. Once we add the
color and the reset code we really need to put each item on it's own line.

## eightball04

```python
#!/usr/bin/env python3

import colors as c

print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    c.green + 'Yes.' + c.reset,
    c.red + 'No.' + c.reset,
    c.base01 + 'Maybe.' + c.reset
]

question = input('> ' + c.yellow)
```

Remember the [`hi`](../hi) program? Remember how we make it wait for a
user to type some input in? Let's do the same thing to prompt the user
for a question they want answered. We'll save what they type into a
`question` variable so we can check it later.

## eightball05

```python
#!/usr/bin/env python3

import colors as c

print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    c.green + 'Yes.' + c.reset,
    c.red + 'No.' + c.reset,
    c.base01 + 'Maybe.' + c.reset
]

question = input('> ' + c.yellow)

import random
answer = random.choice(answers)
print(answer)
```

Now comes the magic, the
[`random`](https://docs.python.org/3.4/library/random.html)
magic. There are lots of [spells in the
random](https://docs.python.org/3.4/library/random.html)
book of code magic. (Ok, fine, it's called a *module*,
but spellbook sounds so much awesome-er.) We'll just use
one [cantrip](http://en.wikipedia.org/wiki/Cantrip) for now:
`random.choice(list)`. This function is like a hat that you put all the
items from your list into and randomly pull one out and *return* it. We'll
save the randomly selected answer into a *variable* named `answer`. Note
the difference between the variables `answer` and `answers`. One is *singular* (just one), and the other *plural*
(more than one).

At this point you have a working, one-time-use magic eight ball. Run it
and see.

## eightball06

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    answer = random.choice(answers)
    print(c.random_color() + answer + c.reset)
```

The rest is just polish. 

Let's move `import random` to the top now where it belongs.

Plus we want to have conversations with our magic eight ball when we are
*really* lonely. ;) Can you think of how you would make this program
repeat answering questions forrreevvaaa? You've done it before. Yep,
you got it, add an infinite loop with `while True:`. Don't forget to
tab/indent your lines over so they are included in the loop block and
don't put your `answers` list inside the loop. You don't need to waste the
computer's time redefining the list every time because it isn't changing.

What else, humm? Ok, let's have at least 20 answers like the actual magic
eight ball. You can make your own 20 answers unique. And no one says you
have to stop with just 20. Go crazy. PG would be awesome, but we don't
judge here. Just please consider your audience.

Annnnnd, because we are lazy, let's take out all the color codes from
the answers list and use a `c.random_color()` instead.

If you got stuck in the `eightball` program and can't get out it is because
you forgot about `<control>-c` that you learned in [`nyan`](../nyan).

## eightball07

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    if question == 'bye':
        print('Goodbye')
        exit()
    answer = random.choice(answers)
    print(c.random_color() + answer + c.reset)
```

But who really wants to have to `<control>-c` to interrupt the
conversation with the magic eight ball, which you have to admit is
rather rude. Let's add a proper goodbye. 

You will likely remember the `if` statement from
[CodeCombat](http://codecombat.com). If not here it is. Like `while`
the `if` statement tests if a question (called a *condition*) is `True`
or `False. There are a whole bunch of different questions and types of
questions you can ask that we will get into more later. For now we only
have one question ask: did the user type ‘bye’ or ‘goodbye’? To put the
question in a from Python understands we have to use two equals signs `==`
together (because a single equals sign is used for assigning variables). So
the question we want to ask is `if question == 'bye'` and we add a block after
it to tell Python what to do if the answer to that question is `True`. We
add another new function `exit()` to the block so that the program stops
politely if the user enters ‘bye’ as their question (instead of an actual
question).

## eightball08

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    if question == 'bye':
        print('Goodbye')
        exit()
    elif question == 'goodbye':
        print('Goodbye')
        exit()
    answer = random.choice(answers)
    print(c.random_color() + answer + c.reset)
```

We only handled if the user types ‘bye’ before but what if the user
enters ‘goodbye’ instead? The `if` statement actually has three parts:
`if`, `elif`, and `else`. We can handle ‘goodbye’ with an `elif
question == 'goodbye'` block. Like before we need to include the code we
want, which happens to be identical to the code from the `if question ==
'bye'` block.

Yes, the answer to your question is there is a better way, a lazier way.

## eightball09

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    if question == 'bye' or question == 'goodbye':
        print('Goodbye')
        exit()
    answer = random.choice(answers)
    print(c.random_color() + answer + c.reset)
```

Here's a new thing: the keywords `or` and `and` also. Just like in
English these allow us to combine two questions into one in our `if`
or `elif` condition checks. Combining two questions into one creates
what's called a *compound condition check*, which is coder-speak for,
well, more than one question at a time. All we really need to remember is
that unlike English we have to include the full question (*condition*)
for each question instead of chopping off the subject of the question
like we often do when speaking. For example, in English we say, “if
question is ‘bye’ or ‘goodbye’” when we mean, “if question
is ‘bye’ or question is ‘goodbye’”. **Full questions are
important. Leaving off the extra `question ==` in the second question
will not give you an error, but also not do what you think.**

```python
if question == 'bye' or 'goodbye':               # <--- WRONG
    print('always prints because never false')
 ```

The reason for this is a little complicated and will be more
understandable later. For now just know that the word 'goodbye' by
itself is seen by Python as `True`. It turns out an empty string is
`False`. This is very useful later on.

## eightball10

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    if question == 'bye' or question == 'goodbye':
        print('Goodbye')
        exit()
    elif 'love' in question:
        print('Do I look like Cupid to you?')
        continue
    elif 'die' in question or 'death' in question or 'dead' in question:
        print("Such grim questions don't deserve an answer, yet.")
        continue
    answer = random.choice(answers)
    print(c.random_color() + answer + c.reset)
```

We may have removed the `elif` for ‘bye’ and ‘goodbye’ but
what if we add it back to add an *Easter Egg* of sorts, you know, those
things coders put in games that are kind of secrets. What if we don't
want users asking about love or death? We'll add two more `elif`s. The
keyword `continue` makes the `while` continue without finishing all the
rest of the code in the loop block.

## eightball11

```python
#!/usr/bin/env python3

import random
import colors as c

print(c.clear)
print(c.red + '''
Welcome to the magic eight ball!
Enter your question below.
''' + c.reset)

answers = [
    'It is certain.',
    'It is decidedly so.',
    'Without a doubt.',
    'Yes definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.'
]

while True:
    question = input('--> ' + c.yellow)
    if question == 'bye' or question == 'goodbye':
        print('Goodbye')
        exit()
    elif 'love' in question:
        print('Do I look like Cupid to you?')
    elif 'die' in question or 'death' in question or 'dead' in question:
        print("Such grim questions don't deserve an answer, yet.")
    else:
        answer = random.choice(answers)
        print(c.random_color() + answer + c.reset)
```

Perhaps a better way to save us from the `continue`s is to simply add
the third part of the `if/elif/else` trio. We add `else:` (don't forget
the colon) and put the code we want to run inside the `else:` block by
indenting it over. Now that code will only run if and only if the `if`
question isn't true and neither of the `elif`s are either.

You may be wondering why not make a bunch of `if` statements instead of
using the `elif` statement at all. The short answer is that it is more
correct and faster. If we only used `if` statements every one would be
checked even if the first one was true. Using `elif` ensures that as
soon as one of the conditions is true that the rest of the `elif`s aren't
even checked and the code skipped. The first `True` wins so to speak. If
none of the `if` and `elif`s are `True` then `else` wins.

## More ...

That's about it. Have fun with this one by adding different responses and
see if you can even add a multi-line ASCII Art answer.
