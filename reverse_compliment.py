def find_rc(rc):
    rc = rc[:: -1]
    replacements = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    rc = "".join([replacements.get(c, c) for c in rc])
    return rc


print(find_rc('ATTA'))
