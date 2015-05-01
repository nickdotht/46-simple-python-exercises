"""According to Wikipedia, a semordnilap is a word or phrase that spells 
a different word or phrase backwards. ("Semordnilap" is itself 
  "palindromes" spelled backwards.) Write a semordnilap recogniser that 
accepts a file name (pointing to a list of words) from the user and finds 
and prints all pairs of words that are semordnilaps to the screen. 
For example, if "stressed" and "desserts" is part of the word list, the 
the output should include the pair "stressed desserts". Note, by the way, 
that each pair by itself forms a palindrome!"""

# Solution by Nick Rameau - @R4meau
import string
file_name = raw_input('Enter file name (ex. semordnilaps.txt)> ')
unwanted = string.punctuation + ' '

def clean(str):
  cleaned_str = filter(lambda x: x not in unwanted, str.rstrip().lower())
  return cleaned_str

found = []
with open(file_name, 'r') as f:
  for line in f:
    if clean(line)[::-1] in found:
      print clean(line), clean(line)[::-1]
    else:
      found.append(clean(line))

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.