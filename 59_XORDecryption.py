# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
# then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target
# As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message
# and find the sum of the ASCII values in the original text.

import itertools

# given a list of encrypted ascii values and a key returns the attempted decryption
def decrypt(encrypted, key):
  ret = []
  i = 0
  while (i < len(encrypted)):
    ret.append(encrypted[i] ^ key[0])
    ret.append(encrypted[i + 1] ^ key[1])
    ret.append(encrypted[i + 2] ^ key[2])
    i = i + 3
  return ret

# scoring function to see how likely this decryption is correct
def score(ascii):
  bad = 0
  good = 0
  for a in ascii:
    # look for all chars A-z and spaces
    if (a >= 65 and a <= 90) or (a >= 97 and a <= 122) or a == 32:
      good = good + 1
    else:
      bad = bad + 1
  return good / (good + bad)
        
def solve():
  f = open("cipher.txt", "r")
  encrypted = f.read().split(',')
  chars = [int(i) for i in encrypted]

  # we know the key is going to be a collection of three lower case ascii values
  keys = list(itertools.product(range(97,123), repeat=3))

  # try all keys and look for anything with a high enough score
  # this heuristic was chosen mostly at random but seemed to work
  for key in keys:
    d = decrypt(chars, key)
    s = score(d)
    if (s > .9):
      text = (''.join([chr(i) for i in d]))
      # print the message for fun
      print(text)
      return sum(d)

print(solve())
