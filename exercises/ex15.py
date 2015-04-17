""" Write a function find_longest_word() that takes 
a list of words and returns the length of the longest one."""

# Solution by Nick Rameau - @R4meau
def find_longest_word(lst):
  longest = ""
  for w in lst:
    if len(w) > len(longest):
      longest = w
  return len(longest)

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print find_longest_word(['hello', 'world', 'Python'])
print find_longest_word(['Live', 'laugh', 'love'])
print find_longest_word(['I', 'found', 'Haiti'])