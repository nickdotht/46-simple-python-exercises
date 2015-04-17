"""Write a program that maps a list of words into a list 
of integers representing the lengths of the correponding words."""

# Solution by Nick Rameau - @R4meau
def words_length(lst):
  lenlist = [len(i) for i in lst]
  return lenlist

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print words_length(['Hello', 'world!'])
print words_length(['Python', 'is', 'awesome!'])
print words_length(['You', 'said', 'it', 'bro!'])