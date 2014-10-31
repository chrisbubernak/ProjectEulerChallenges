#If the numbers 1 to 5 are written out in words: one, two, three, four,
#five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written
#out in words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
#and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#contains 20 letters. The use of "and" when writing out numbers is in
#compliance with British usage.

numToWordDict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
    1000: 'one thousand'
}

def numToWord(num):
    if num in numToWordDict.keys():
        return numToWordDict[num];

    num = str(num);
    l = len(num);
    start = numToWordDict[int(num[0] + ("0" * (l -1)))];
    if l == 2:
        connector = "-";
    elif l == 3:
        connector = " and ";
    end = numToWord(int(num[1:]));
    return start + connector + end;
def countOfLetters(word):
    ret = 0;
    for char in word:
        if not(char == " " or char == "-"):
            ret = ret + 1;
    return ret;

def solve(n):
    ret = 0;
    for i in range(1, n+1):
        ret = ret + countOfLetters(numToWord(i));
    return ret;

print solve(1000);
