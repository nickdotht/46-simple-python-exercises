"""Implement the higher order functions map(), filter() and reduce(). 
(They are built-in but writing them yourself may be a good exercise.)"""
# Solution by Nick Rameau - @R4meau
# map() implementation. I know I didn't fully implement it because it would 
# be kinda long, but that's the basic
def map(function, sequence):
  result = []
  for item in sequence:
    result.append(function(item))
  return result

# filter() implementation  
def filter(function, sequence):
  # If sequence is a tuple or string, return the same type, 
  # else return a list.
  if isinstance(sequence, tuple):
    result = ()
  elif isinstance(sequence, str):
    result = ''
  else:
    result = []
    
  for item in sequence:
    if function(item):
      if isinstance(sequence, tuple):
        result += (item,)
      elif isinstance(sequence, str):
        result += item
      else:
        result.append(item)
  return result

# reduce() implementation
def reduce(function, sequence, initial=None):
  result = initial if initial else sequence[0]
  if initial:
    for item in sequence:
      result = function(result, item)
  else:
    for item in sequence[1:]:
      result = function(result, item)
  return result


# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print map(lambda x: x * 2, [1,2,3,4])
print filter(lambda x: x.endswith('in'), ('lapin', 'cretin', 'ah', 'oui'))
print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 5)