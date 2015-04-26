"""Write a function find_longest_word() that takes a list of words and 
returns the length of the longest one. Use only higher order functions."""

# Solution by Nick Rameau - @R4meau
def find_longest_word(words):
  return max(map(len, words))

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print find_longest_word(['This', 'is', 'unacceptable'])