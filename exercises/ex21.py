"""Write a function char_freq() that takes a string and builds 
a frequency listing of the characters contained in it. Represent 
the frequency listing as a Python dictionary. Try it with something 
like char_freq("abbabcbdbabdbdbabababcbcbab")."""

# Solution by Nick Rameau - @R4meau
import string
def char_freq(str):
  freq = {}
  for c in str:
    freq[c] = string.count(str, c)
  return freq

# Solution by Nick Rameau - @R4meau
# def char_freq(str):
#   freq = {}
#   for c in str:
#     if c in freq:
#       freq[c] += 1
#     else:
#       freq[c] = 1
#   return freq
      

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print char_freq("abbabcbdbabdbdbabababcbcbab")
print char_freq("hello")