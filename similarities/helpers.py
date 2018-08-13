from nltk.tokenize import sent_tokenize

def indenticalItems(listA, listB):

    indenticalItems = []

    for item in listA:
        if (item in listB and item not in indenticalItems):
            indenticalItems.append(item)

    return indenticalItems

def stringToListOfSubstrings(string, length):

    index = 0
    newString = " ".join(string.splitlines())
    substrings = []

    while (index < len(newString)):
        if (length <= len(newString[index:length+index])):
            substrings.append(newString[index:length+index])
        index += 1

    print(substrings)
    print('')

    return substrings

def lines(a, b):
    """Return lines in both a and b"""

    return indenticalItems(a.splitlines(), b.splitlines())


def sentences(a, b):
    """Return sentences in both a and b"""

    return indenticalItems(sent_tokenize(a), sent_tokenize(b))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    substringsA = stringToListOfSubstrings(a, n)
    substringsB = stringToListOfSubstrings(b, n)

    return indenticalItems(substringsA, substringsB)
