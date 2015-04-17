"""Define a function is_palindrome() that recognizes 
palindromes (i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True."""

# Solution by Nick Rameau - @R4meau
def is_palindrome(str):
  return str == str[::-1]

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print is_palindrome("radar")
print is_palindrome("IzitizI")