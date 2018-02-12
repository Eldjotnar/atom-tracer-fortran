# Atomic Tracer

A language agnostic Atom package for tracing variables inline! 

It shows you where a variable was declared and its value at each line thereafter:

![simple_example](https://raw.githubusercontent.com/OmarShehata/atom-tracer/master/_images/tracer_simple.gif)

If a line of code is executed more than once, you can see all the values it had in a list:

![for_example](https://raw.githubusercontent.com/OmarShehata/atom-tracer/master/_images/tracer_for.gif)

It also works on function arguments:

![funcexample](https://raw.githubusercontent.com/OmarShehata/atom-tracer/master/_images/tracer_func.gif)

The tracer originally supported only Python, but it now supports Fortran 90, 95, 2003, and 2008 (and soon C++ hopefully)!

# About My Work

This project was created by Omar Shehata, a fellow student of mine at St. Olaf, for tracing variables in python. For my Programming Languages Class (Fall '17), I elected to expand and optimize it to support Fortran, and work more efficiently.  

# Installation

This package depends on [Ink](https://github.com/JunoLab/atom-ink), so install that one first. 

Then install the tracer from your Atom settings, or through `apm`:

```
apm install atom-tracer
```

If you plan on tracing Fortran in atom, it's probably a good idea to install a [syntax-highlighting package](https://atom.io/packages/language-fortran).

# Usage

Once installed, you can hold Alt and double click on a variable to trace it. Double click anywhere in the file to clear the results.

Click on the result box to copy its contents.

You can also select a variable, right click and click on "Trace variable" in the context menu.

# What is this for?

This is not a very sophisticated debugger (for one thing, you can't trace anything that requires user input). It's intended to be used as a teaching tool.

I created this because I think learning to reason about code and debug it is an important skill, and not having an easy way to see the flow of execution hinders that. I wanted to have a tool that made it transparent to the student what was happening throughout the lifetime of a variable in an effort to check their understanding.

# How does it work?

It parses the abstract syntax tree to find where the variable is declared and what its scope is, and then injects print statements into the file, runs it, captures the output, and displays it inline.

If you want more details, see this [page](HowItWorks.md)!

This is built on top of the awesome [Ink](https://github.com/JunoLab/atom-ink) package!
