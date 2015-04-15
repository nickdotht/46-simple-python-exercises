"""Define a function max() that takes two numbers as arguments 
and returns the largest of them. Use the if-then-else construct 
available in Python. (It is true that Python has the max() function 
  built in, but writing it yourself is nevertheless a good exercise.)"""

# Solution by Nick Rameau - @R4meau
def max(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'd be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print max(3, 5)
print max(10, 6)