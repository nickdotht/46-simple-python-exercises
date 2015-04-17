"""Write a function filter_long_words() that takes a list 
of words and an integer n and returns the list of words that 
are longer than n."""

# Solution by Nick Rameau - @R4meau
def filter_long_words(lst, n):
  return [w for w in lst if len(w) > n]


# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print filter_long_words(['Hello', 'world', 'Haiti', 'Pythonistas!'], 5)
print filter_long_words(['Python', 'stole', 'my', 'heart'], 4)
print filter_long_words(['This', 'will', 'be', 'cool'], 3)