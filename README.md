# Learning to Program, in Python

![](https://www.python.org/static/community_logos/python-logo-generic.svg)

Meet Python, the best first programming language anyone should learn.
It is approachable, easy, and &mdash; most of all &mdash; real. Python is
a core language used by the worldwide scientific community &mdash; including
MIT where it is the first language taught. Python can be found everywhere
from elementary schools to Hollywood &mdash; even on the cover of the
Bloomberg Businessweek dedicated to coding:


![](img/bloomberg.jpg)

# What We Learn

In this course students find out what coding is, why they should learn it,
and how. Students focus on programming fundamentals such as variables,
operators, blocks, logic, loops, data types, lists, dictionaries,
functions, exceptions, unit testing, and basic code organization.

Students gradually learn the same habits, tools, and workflows associated
with college computer science programs and technical careers. We
write code using vim from the command-line the way most experienced
professionals do.

Students learn modern Python 3 (not 2.7) for many obvious reasons.

# What We Don't Learn

Python-1 focuses on basic structured and procedural programming
paradigms. It does not directly cover important but more advanced concepts
such as traditional object-oriented and functional programming.  While the
games and code in Python-1 are designed to be fun, Python-1 does **not**
use Python IDLE, `turtle`, `pygame` or other made-for-education Python
technologies, which, despite their prevalence, are of dubious value in
the higher-education and professional world. Focus is placed instead on
techniques and tools that will remain useful well beyond school. Students
are encouraged to unit test their code often but no test frameworks
besides code bits in `if __name__ == '__main__':` are introduced at
this level.

# Planning

This course takes a total of 24 hours to complete and is designed
to fit into 16 weeks of 90-minute classes (a semester) or two, 4-day weeks of
3-hour classes (ex: 9:30 - 12:30, Monday - Thursday).

The pace is set to what an average 8-12 year-old with typing skills can
accomplish within 70 minutes of a 90 minute class. Bonus challenges are
available for faster and older learners increasing the age range to about 18.
Keep in mind, however, that adults are also challenged by this material
(even if they don't get the pop references).

The last two weeks are a review of all the previous material. Avoid the
temptation to skip the final review since it ensures students are ready to
progress.

**Week 1:** [hello](/hello) - vim, `chmod`, `#!`, strings, functions, `print()`, `import colors`, `+`,`"`,`'`<br>
**Week 1:** [hi](/hi) - `input()`, variables, assignment, operators, `=`<br>
**Week 2:** [nyan](/nyan) - code blocks, booleans, `while`, `True/False`,`ctrl-c`, `'''`, `end=''`, ascii, `top`<br>
**Week 3:** [waffles](/waffles) - conditions, `if/else`, `==`, nested blocks, exceptions, `try/except`, `exit()`<br>
**Week 4:** [dice](/dice) - lists, loops, `for`, `range()`, implicit,`.append()`,`import random`,`.choice()`<br>
**Week 5:** [badgers](/badgers) - numbers, casting, `int/str()`, nesting, scope, `import time`, `.sleep()`<br>
**Week 6:** [eightball](/eightball) - `if/elif/else`, `not`, `!=`, `in`, `.strip()`, `.lower()`<br>
**Week 7:** [bridge](/bridge) - compound conditions, `or`, `and`, logic bugs, functions, `def`, `return`<br>
**Week 7:** [bridge](/bridge) - procedures<br>
**Week 8:** [cli.py](/cli) - basic modules, refactoring, reuse, docstrings, `if
__name__ == '__main__':`<br>
**Week 9:** [mtable](/mtable) - math, `*` vs `x`, `for`,`range()`, arguments, `import sys`,`argv`,`len()`<br>
**Week 10:** [madforms](/madforms) - dictionaries, JSON, web apis, `.format()`<br>
**Week 11:** [madforms](/madforms) - `for`, `.splitlines()`, `.rstrip()`<br>
**Week 12:** [bincount](/bincount) - decimal (base 10), binary (base 2), hexadecimal (base 16), `.format()`<br>
**Week 13:** [quiz](/quiz) - first-class functions, modules, scope `import`<br>
**Week 14:** [quiz](/quiz) - `$PYTHONPATH`, conditional `import`<br>
**Week 15:** [review](/review) - hello, hi, nyan, waffles, dice, badgers,
eightball<br>
**Week 16:** [review](/review) - bridge, cli.py, mtable, madforms, bincount,
quiz<br>

# Resources and Requirements

[![][logo]][scb] [![][cc0]][cc0link]

Students need access to a Linux command-line on a computer that has had
`python3` installed. Usually this will be through an ssh connection
(putty, etc.) to a Linux account on a school server. This could equally
be done with individual [Raspberry Pi][] computers, individual Linux
real or virtual machines, or a remote virtual host such as Digital Ocean.

GitHub accounts for each student are strongly recommended and the
`bin/save` can make commits easier.

[logo]: http://skilstak.com/images/skilstak-logo-bw-31.svg "SkilStak"
[scb]: README-SKB.md
[cc0]: http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg "CC0 Public Domain"
[cc0link]: https://creativecommons.org/publicdomain/zero/1.0/
[Raspberry Pi]: https://www.raspberrypi.org/
