### [46 Simple Python exercises](http://www.ling.gu.se/~lager/python_exercises.html)

This list of exercises comprises logical operators, loops, input and output, regular expressions and more in order for people to have a basic overview of the language.

They might not be the best solutions, but I'd be glad to pull your requests.

This repository contains solutions to all 46 exercises I have solved. They're intended as a last resort in case you've tried very hard to solve a problem but you just haven't been able to figure it out.

I made sure to comment the hardest ones, or the ones that gave me some trouble.


### Using Python 3?

I implemented all the solutions using Python 2.7.1 but if you're using Python 3.x most of the solutions won't work for you.
That's why I created a converter for you to convert all the solutions into Python 3. 
In the project folder you will notice two files:

-- *makepython3.py* A converter that uses the 2to3 command

-- *make_python3.py* A converter that uses regular expressions

You don't have to use both, but I recommend running the one using the 2to3 command because it is the official way to convert 2.7 to 3.x. The latter one is just me using my regex skills to do the conversion, you might wanna have a look at it to understand how it works ;)

So all you need to do after downloading the project is

```bash
cd 46-simple-python-exercises
python makepython3.py
```

And it will create a folder called *exercisespy3* in the same directory. In this folder you will find all the solutions in Python 3.x.

Enjoy.