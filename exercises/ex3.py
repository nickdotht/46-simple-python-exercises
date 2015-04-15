"""Define a function that computes the length of a 
given list or string. (It is true that Python has 
the len() function built in, but writing it yourself 
is nevertheless a good exercise.)"""

# Solution by Nick Rameau - @R4meau
def length(str):
  count = 0
  for i in str:
    count += 1
  return count

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'd be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print length("Hello, world!")
print length("Nick was here.")
print length("Cool")