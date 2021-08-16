def list_to_string(lst):
    string = ''
    for item in lst:
        string = string + item
    return string


def find_rc(rc):
    rc = rc[:: -1]
    replacements = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    rc = "".join([replacements.get(c, c) for c in rc])
    return rc


def find_palindromes(x):
    sequence = list(x.upper())
    end_index = 4
    palindromes = []
    count = 0
    for i in range(0, len(sequence) - 1):
        rc = find_rc(sequence[i:end_index])
        original = sequence[i:end_index]
        end_index += 1
        if rc == list_to_string(original):
            palindromes.append(i)
            count += 1

    str_palindromes = ''
    for item in palindromes[0:len(palindromes) - 1]:
        str_palindromes += str(item)
        str_palindromes += ', '

    return count, str_palindromes


dna = str(input('Enter seq: '))
print('there are', find_palindromes(dna)[0], 'palindromes at places', find_palindromes(dna)[1], '\n')
