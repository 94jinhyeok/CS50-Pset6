from nltk.tokenize import sent_tokenize

def indenticalItems(listA, listB):

    indenticalItems = []

    for item in listA:
        if (item in listB and item not in indenticalItems):
            indenticalItems.append(item)

    return indenticalItems

def stringToListOfSubstrings(string, length):

    index = 0

    substrings = []

    while (index < len(" ".join(string.splitlines()))):
        if (index % length == 0):
            substrings.append(" ".join(string.splitlines())[index:length+index:1])
        index += 1

    print(substrings)

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
