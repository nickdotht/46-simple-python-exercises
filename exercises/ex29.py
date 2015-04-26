"""Using the higher order function filter(), define a function 
filter_long_words() that takes a list of words and an integer n 
and returns the list of words that are longer than n."""

# Solution by Nick Rameau - @R4meau
def filter_long_words(words, n):
  return filter(lambda x: len(x) > n, words)

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print filter_long_words(['that', ' was', 'not', 'funny', 'at', 'all'], 3)