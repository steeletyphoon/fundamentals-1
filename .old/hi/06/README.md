## The Prompt Challenge

```python
#!/usr/bin/env python3

import colors as c

print(c.clear + c.yellow + "Hi, what's your name?")
name = input(c.orange + '--> ')
print(c.yellow + 'Well ' + name + ', nice to meet you.')
```
Now, can you figure out how to make the `-->` prompt a different color than
what the user types in? Give it a try before you proceed.
