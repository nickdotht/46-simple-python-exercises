"""Define a function generate_n_chars() that takes an 
integer n and a character c and returns a string, n 
characters long, consisting only of c:s. For example, 
generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" 
that will evaluate to "xxxxx". For the sake of the exercise you should 
ignore that the problem can be solved in this manner.)"""

# Solution by Nick Rameau - @R4meau
def generate_n_chars(n, str):
  result = ""
  for x in xrange(n):
    result += str
  return result

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print generate_n_chars(5, "x")
print generate_n_chars(10, "*")
print generate_n_chars(2, "Hello")