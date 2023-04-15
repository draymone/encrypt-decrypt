import string


def convert_for_polybe(text):
    """Takes in argument a text (string)
    Returns the text converted for being used in the polybe encoding"""
    text = text.upper()  # Make the text uppercase

    i = 0
    while i < len(text):  # Replace W by VV
        if text[i] == "W":
            text = text[:i] + "VV" + text[i+1:len(text)]
        i += 1

    i = 0
    uppercases = list(string.ascii_uppercase)
    while i < len(text):  # Remove non numeric characters
        if not text[i] in uppercases:
            text = text[:i] + text[i+1:len(text)]
            i -= 1
        i += 1

    return text


def get_polybius_square():
    """Takes no argument
    Returns a 5x5 array containing the letters of the alphabet"""
    letters = list(string.ascii_uppercase)
    letters.remove("W")
    polybius_square = [[], [], [], [], []]

    for i in range(5):
        sublist = []
        for j in range(5):
            sublist += letters[5*i + j]
        polybius_square[i] = sublist

    return polybius_square


def polybe_encode(text):
    """Takes in argument a text (string)
    Returns the text encoded with Polybius square"""
    # TODO Polybe encode


def polybe_decode(text):
    """Takes in argument a text (string)
    Returns the text decoded by Polybius square"""
    # TODO Polybe decode


