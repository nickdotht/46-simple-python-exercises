"""Write a version of a palindrome recognizer that also accepts 
phrase palindromes such as "Go hang a salami I'm a lasagna hog.", 
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", 
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", 
"I roamed under it as a tired nude Maori", "Rise to vote sir", or 
the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, 
and spacing are usually ignored."""

# Solution by Nick Rameau - @R4meau
import string

ignored = string.punctuation + " "

def is_palindrome(str):
  cleanstr = ""
  for i in str:
    cleanstr += "" if i in ignored else i # I love Python ternary operator

  return cleanstr.lower() == cleanstr[::-1].lower()

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print is_palindrome("Go hang a salami I'm a lasagna hog.")
print is_palindrome("Was it a rat I saw?")
print is_palindrome("Step on no pets")
print is_palindrome("Sit on a potato pan, Otis!")
print is_palindrome("Lisa Bonet ate no basil")
print is_palindrome("Satan, oscillate my metallic sonatas")
print is_palindrome("I roamed under it as a tired nude Maori")
print is_palindrome("Rise to vote sir")
print is_palindrome("Dammit, I'm mad!")
print is_palindrome("This is not a palindrome")