"""Using the higher order function reduce(), write a function max_in_list() 
that takes a list of numbers and returns the largest one. Then ask yourself:
why define and call a new function, when I can just as well call the reduce() 
function directly?"""

# Solution by Nick Rameau - @R4meau
def max_in_list(lst):
  return reduce(lambda x, y: x if x > y else y, lst)

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print max_in_list([1,2,3,4,5,6,10,3])