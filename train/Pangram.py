def isPangram(s):
    s = ''.join(set(s))
    isPangram = len(s.lower().replace(" ", "")) == 26
    if isPangram:
        return "pangram"
    else:
        return "no pangram"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # s = s.lower()
    # for char in s:
    #     print(char)
    #     alpha = alpha.replace(char, "")
    #     print(alpha)
    #     s = s.replace(char, "")
    #
    # if len(alpha) == 0:
    #     return "pangram"
    # else:
    #     return "no pangram"


def testprint():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    print(alpha)
    alpha = alpha.replace("a", "0")
    print(alpha)


if __name__ == '__main__':
    # s = "The quick brown fox jumps over the lazy dog"
    # s = "We promptly judged antique ivory buckles for the next prize"
    s = "We promptly judged antique ivory buckles for the next prize"
    print(isPangram(s))
    # testprint()
