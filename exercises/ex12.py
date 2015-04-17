"""Define a procedure histogram() that takes a list of 
integers and prints a histogram to the screen. For example, 
histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

# Solution by Nick Rameau - @R4meau
def histogram(lst):
  for n in lst:
    print n * "*"
  print 10 * "-" # Just to add some space between each test

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
histogram([4,9,7])
histogram([5,6,8])
histogram([10,8,19])