"""Write a function translate() that will translate a text 
into "rovarspraket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence 
of "o" in between. For example, translate("this is fun") 
should return the string "tothohisos isos fofunon"."""

# Solution by Nick Rameau - @R4meau
import string

all_letters = string.ascii_letters
vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = [chr for chr in all_letters if chr not in vowels]

def robberlang(str):
  result = ""
  for c in str:
    if c in consonants:
      result += c+'o'+c
    else:
      result += c
  return result

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'd be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print robberlang("This is kinda fun")
print robberlang("I Think YoU Might BE righT!")