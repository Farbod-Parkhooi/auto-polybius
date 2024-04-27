let_letters = {
    "A":"11",
    "B":"21",
    "C":"31",
    "D":"41",
    "E":"51",
    "F":"12",
    "G":"22",
    "H":"32",
    "I":"42",
    "J":"42",
    "K":"52",
    "L":"13",
    "M":"23",
    "N":"33",
    "O":"43",
    "P":"53",
    "Q":"14",
    "R":"24",
    "S":"34",
    "T":"44",
    "U":"54",
    "V":"15",
    "W":"25",
    "X":"35",
    "Y":"45",
    "Z":"55"
}
num_letters = {
    "11":"A",
    "21":"B",
    "31":"C",
    "41":"D",
    "51":"E",
    "12":"F",
    "22":"G",
    "32":"H",
    "42":"I(I or J)",
    "52":"K",
    "13":"L",
    "23":"M",
    "33":"N",
    "43":"O",
    "53":"P",
    "14":"Q",
    "24":"R",
    "34":"S",
    "44":"T",
    "54":"U",
    "15":"V",
    "25":"W",
    "35":"X",
    "45":"Y",
    "55":"Z"
}

def decode(text):
    text = text.split("-")
    lets = []
    out = """"""
    # add each two letters in lets list
    for i in range(len(text)):
        nums = len(text[i])
        for j in range(int(len(text[i])/2)):
            data = text[i][-nums] + text[i][-(nums-1)]
            lets.append(data)
            nums -= 2
        lets.append("-")
    # convert lets list's values to letters
    for i in range(len(lets)):
        try: out += num_letters[lets[i]]
        except KeyError: 
            if lets[i] == "-": out += " "
            else: out += lets[i]
    return out
def encode(text):
    out = """"""
    # convert letters to numbers
    for letter in text:
        if letter == " ": out += "-"
        else: 
            try: out += let_letters[letter.upper()]
            except: out += letter
    return out