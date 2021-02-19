# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). 
# But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie 
# then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD    2C 3S 8S 8D TD  Player 2
#       Pair of Fives     Pair of Eights
# 2	 	5D 8C 9S JS AC    2C 5C 7D 8S QH  Player 1
#       Highest card Ace  Highest card Queen
# 3	 	2D 9C AS AH AC    3D 6D 7D TD QD
#       Three Aces        Flush with Diamonds  Player 2 
# 4	 	4D 6S 9H QH QC    3D 6D 7H QD QS
#       Pair of Queens    Pair of Queens  Player 1
#       Highest card Nine Highest card Seven
# 5	 	2H 2D 4C 4D 4S    3C 3D 3S 9S 9D
#       Full House        Full House
#       With Three Fours  with Three Threes  Player 1

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five 
# are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand 
# is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

cardValues = { 'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10} 

# returns the suit of a card: C, H, D, S
def suit(card):
  return card[1]

# returns the value of a card: 2 -> 12
def value(card):
  val = card[0]
  if val in cardValues:
     return cardValues[val]
  return int(card[0])

def isStraight(cards):
  cards.sort(key=lambda x: value(x))
  for i in range(0, len(cards) - 1):
    if not(value(cards[i]) == value(cards[i + 1]) - 1):
      return False
  return True

def isFlush(cards):
  return all(suit(card) == suit(cards[0]) for card in cards)

def isFullHouse(cards):
  cards.sort(key=lambda x: value(x))
  firstThreeEqual = all(value(card) == value(cards[0]) for card in cards[0:3])
  lastTwoEqual = all(value(card) == value(cards[3]) for card in cards[3:5])

  firstTwoEqual = all(value(card) == value(cards[0]) for card in cards[0:2])
  lastThreeEqual = all(value(card) == value(cards[0]) for card in cards[2:5])

  return (firstThreeEqual and lastTwoEqual) or (firstTwoEqual and lastThreeEqual)

def isTwoPair(cards):
  pairs = 0
  vals = dict()
  for card in cards:
    v = value(card)
    if not(v in vals):
      vals[v] = 0
    vals[v] = vals[v] + 1
  for v in vals:
    if (vals[v] == 2):
      pairs = pairs + 1
  return pairs == 2 

def nOfAKind(cards, n):
  vals = dict()
  for card in cards:
    v = value(card)
    if not(v in vals):
      vals[v] = 0
    vals[v] = vals[v] + 1
  for v in vals:
    if (vals[v] == n):
      return True
  return False 

def score(cards):
  cards.sort(key=lambda x: value(x))
  flush = isFlush(cards)
  straight = isStraight(cards)
  straightFlush = flush and straight
  fourKind = nOfAKind(cards, 4)
  fullHouse = isFullHouse(cards)
  threeKind = nOfAKind(cards, 3)
  twoPair = isTwoPair(cards)
  twoKind = nOfAKind(cards, 2)
   
  if straightFlush:
    return 9
  elif fourKind:
    return 8
  elif fullHouse:
    return 7
  elif flush:
    return 6
  elif straight:
    return 5
  elif threeKind:
    return 4
  elif twoPair:
    return 3
  elif twoKind:
     return 2
  else:
    return 1

# returns which value appears N times in a hand
def nOfAKindVal(cards, n):
  vals = dict()
  for card in cards:
    v = value(card)
    if not(v in vals):
      vals[v] = 0
    vals[v] = vals[v] + 1
  for v in vals:
    if (vals[v] == n):
      return v
  # error!
  return -1 

# breaks a tie if two hands havae the same score/rank
def breakTie(hand1, hand2, score):
  if score == 9 or score == 6 or score == 5 or score == 1:
    return highestCard(hand1, hand2)
  if score == 2:
    pair1 = nOfAKindVal(hand1, 2)
    pair2 = nOfAKindVal(hand2, 2)
    if not(pair1 == pair2):
      return pair1 > pair2
    else:
      return highestCard(hand1, hand2)
  # TODO(chris): break ties for rank 3, 4, 7, 8
  return False

# goes through two hands comparing each card (large -> small)
# and as soon as they don't match returns true if hand1 is bigger
# false if hand2 is (or they have all matching cards)
def highestCard(hand1, hand2):
  hand1.sort(key=lambda x: value(x))
  hand2.sort(key=lambda x: value(x))
  for i in range(0, len(hand1)):
    if not(value(hand1[4 - i]) == value(hand2[4 - i])):
      return value(hand1[4 - i]) > value(hand2[4 - i])
  return False

def solve():
  wins = 0
  f = open("poker.txt", "r")
  lines = f.readlines()
  for l in lines:
    cards = l.split()
    player1 = cards[0:5]
    player2 = cards[5:10]
    score1 = score(player1)
    score2 = score(player2)
    if (score1 == score2):
      winsTieBreak = breakTie(player1, player2, score1)
      if winsTieBreak:
        wins = wins + 1
    elif (score1 > score2):
      wins = wins + 1
  return wins

print(solve())
