# The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so
# the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value. For example, the word value
# for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we
# shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

filename = "words.txt";

alphabet = list("abcdefghijklmnopqrstuvwxyz");

def letterValue(l):
    return alphabet.index(l.lower()) + 1;

def wordValue(w):
    total = 0;
    letters = list(w);
    for i in range(0, len(letters)):
        total = total + letterValue(letters[i]);
    return total;

def getT(n):
    return (n*(n+1))/2;

def solve():
    # dict where the keys are numbers corresponding to word value
    # and the values are an array of words that have that value
    dict = {};
    # keep track of the max value so we know when to stop calculating
    # triangle numbers
    maxValue = 0;
    ret = 0;
    txt = open(filename);
    words = txt.read().split(",");
    for i in range(0, len(words)):
        word = words[i].replace("\"", "");
        value = wordValue(word);
        if (value > maxValue):
            maxValue = value;
        if value in dict:
            dict[value].append(word);
        else:
            dict[value] = [word];
    i = 1;
    t = getT(i);
    while(t <= maxValue):
        if t in dict:
            ret = ret + len(dict[t]);
        i = i + 1;
        t = getT(i);
    return ret;


print solve();
