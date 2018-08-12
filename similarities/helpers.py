def lines(a, b):
    """Return lines in both a and b"""

    linesA = a.split('\n')
    linesB = b.split('\n')
    indenticalLines = []

    for line in linesA:
        if (line in linesB and line not in indenticalLines):
            indenticalLines.append(line)

    print(linesA)
    print(linesB)
    print(indenticalLines)

    return []


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
