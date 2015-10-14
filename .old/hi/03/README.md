## Remembering Input

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
assigning it just like we did color codes in `hello`.

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
