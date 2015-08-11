# Ooooo, Pretty Colors

![Solarized Color Palette](http://ethanschoonover.com/solarized/img/solarized-palette.png)

Most classes would stop right here and call this "hello world" complete
but let's add some color. Somehow programming is more fun with colors
and these days adding color to terminal programs is pretty easy. Most
terminals are still limited to 16 colors so we will use the [Solarized
Dark Theme](http://ethanschoonover.com/solarized), our favorite here at
SkilStak. What are the colors you ask? Type `colors` on the command-line
to see:

![`colors` Help Command](colors.png)


To use these fancy colors we have to `import` them. Think of this as
checking out a code book from the library that has extra stuff in it we want
to use that isn't included. The `as c` part tells Python we don't want to
type `colors` every time we use anything from the `colors` module:

```python3
import colors as c
```

Now that it's imported we can change our code to use them:

```python3
print(c.yellow + "Hello world" + c.reset) 
```

We will use long form `c.yellow` for now and short for later to save on
space and typing. When in doubt, use whatever one reads the best.

The `c.reset` is a good habit to get into. It keeps colors from bleeding
into text that follows.

## Setting Up Your Own Colors

If you are a teacher or am ambitious student who does not
have these colors set up in your terminal you can look at
[`tools`](../tools) for some help.
