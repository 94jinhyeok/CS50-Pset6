from nltk.tokenize import sent_tokenize

def indenticalItems(listA, listB):

    indenticalItems = []

    for item in listA:
        if (item in listB and item not in indenticalItems):
            indenticalItems.append(item)

    return indenticalItems

def lines(a, b):
    """Return lines in both a and b"""

    return indenticalItems(a.split('\n'), b.split('\n'))


def sentences(a, b):
    """Return sentences in both a and b"""

    return indenticalItems(sent_tokenize(a), sent_tokenize(b))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
