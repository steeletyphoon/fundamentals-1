# Chmod That SheBang

![](../img/dry.png)

The best programmers live by an important rule *Don't Repeat Yourself*
or *DRY* — even code-muggles can appreciate that. Typing `python3`
is far too much work.  We just want to type `hello`, but how?

## Make It Executable

***Executable*** means *runnable*. It is the difference between a simple
***text file*** and a ***script***. To change this we use the `chmod +x
hello` command. After this the script is a different color and we see an `x`
in the permissions for the file when we do `ls -l hello`:

```
-rwxr-xr-x 1 student student 46 Jul 11 14:57 hello
```

Don't worry about permissions now, just know they control things
like reading and writing the file and telling the computer the file is
a script that can be run.

![](../img/chmod4.png)

## Tell Computer How to Run the Program


After `chmod`ing we have to tell the computer which program we want to use to run
our Python `hello` script. By adding the executable permission we signaled
to the computer to look at the first line of our script for a ***shebang
line***.  This special line starts with a *hashtag* `#` and the *bang*
is for the exclamation point `!`. Coders have all kinds of slang for
different characters. Add the following on the very first line of your script:

```python
#!/usr/bin/env python3
```

Don't forget the space between `env` and `python3` and don't forget the `3`
or put a space before it.

We could have used `#!/usr/bin/python3` but use the `env` version
instead. `env` is itself a program that finds other programs wherever
they are.  `env` finds `python3` wherever it may be on the system
(or another system). This makes our program easier to share with others.

![](../img/shebang.png)
