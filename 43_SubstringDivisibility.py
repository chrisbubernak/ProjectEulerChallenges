#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

def has_property(num_string):
  if (int(num_string[1:4])) % 2 != 0:
    return False
  if (int(num_string[2:5])) % 3 != 0:
    return False
  if (int(num_string[3:6])) % 5 != 0:
    return False
  if (int(num_string[4:7])) % 7 != 0:
    return False
  if (int(num_string[5:8])) % 11 != 0:
    return False
  if (int(num_string[6:9])) % 13 != 0:
    return False
  if (int(num_string[7:10])) % 17 != 0:
    return False
  return True

def pandigital_recurse(cur, remaining):
  if len(remaining) == 0:
    return [cur]
  ret = []
  for i in range(len(remaining)):
    num = remaining[i]
    new_cur = cur + num
    new_remaining = remaining.replace(num,'')
    ret = ret + pandigital_recurse(new_cur, new_remaining)
  return ret

def solve():
  numbers = pandigital_recurse('', '0123456789')
  sum = 0
  for i in range(len(numbers)):
    if has_property(numbers[i]):
      sum = sum + int(numbers[i])
  return sum
    
print solve()
