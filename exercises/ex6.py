"""Define a function sum() and a function multiply() that 
sums and multiplies (respectively) all the numbers in a list 
of numbers. For example, sum([1, 2, 3, 4]) should return 10, 
and multiply([1, 2, 3, 4]) should return 24."""

# Solution by Nick Rameau - @R4meau
def sum(lst):
  result = 0
  for i in lst:
    result += i
  return result

def multiply(lst):
  result = 1
  for i in lst:
    result *= i
  return result

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print sum([1,2,3,4,5])
print multiply([1,2,3,4,5])