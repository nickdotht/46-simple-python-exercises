"""Write a function that takes a character (i.e. a 
string of length 1) and returns True if it is a vowel, 
False otherwise."""

# Solution by Nick Rameau - @R4meau
vowels = ['a', 'e', 'i', 'o', 'u']

def vornot(str):
  if str in vowels:
    return True
  else:
    return False

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'd be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print vornot('e')
print vornot('1')
print vornot('z')