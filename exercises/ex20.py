"""Represent a small bilingual lexicon as a Python dictionary in the 
following fashion {"merry":"god", "christmas":"jul", "and":"och", 
"happy":gott", "new":"nytt", "year":"ar"} and use it to translate 
your Christmas cards from English into Swedish. That is, write a 
function translate() that takes a list of English words and returns 
a list of Swedish words."""

# Solution by Nick Rameau - @R4meau
dictionary = {"merry":"god", "christmas":"jul", "and":"och", 
"happy":"gott", "new":"nytt", "year":"ar"}

def translate(lst):
  return [dictionary[w.lower()] for w in lst if w.lower() in dictionary]
  

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])