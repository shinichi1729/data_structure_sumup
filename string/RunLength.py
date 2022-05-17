from itertools import groupby


# ex) in:"AAABBBAAABA"
#    out:[('A', 3), ('B', 3), ('A', 3), ('B', 1), ('A', 1)]
def runlengthencode(string):
    res = []
    for key, cnt in groupby(string):
        res.append((key, len(list(cnt))))
    return res


# ex) in:[('A', 3), ('B', 3), ('A', 3), ('B', 1), ('A', 1)]
#    out:"AAABBBAAABA"
def runlengthdecode(data):
    res = ""
    for key, cnt in data:
        res += key*cnt
    return res


# ex) in:"AAABBBAAABA"
#    out:"A3B3A3B1A1"
def runlengthencodetostring(string):
    res = ""
    for key, cnt in groupby(string):
        res += key + str(len(list(cnt)))
    return res



if __name__ == '__main__':
    word = "AAABBBBAABBA"
    # encode = runlengthencode(word)
    # encodetostring = runlengthencodetostring(word)
    # decode = runlengthdecode(encode)
    # 
    # print(word)
    # print(f"encode -> {encode}")
    # print(f"encode(str) -> {encodetostring}")
    # print(f"decode {encode} -> {decode}")

