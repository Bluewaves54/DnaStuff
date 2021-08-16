import re


def find_rc(rc):
    rc = rc[:: -1]
    replacements = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}
    rc = "".join([replacements.get(c, c) for c in rc])
    return rc


def get_genome(x):
    f = open(x).readlines()
    for i in f[0]:
        if i != 'A' or 'T' or 'G' or 'C':
            f.remove(f[0])
            break
    dna = ''
    for line in range(0, len(f) - 1):
        dna += f[line].rstrip()

    dna = dna.upper()
    return dna


def find_rest_indexes(x, y):
    split = y.find('/')
    y = y.replace('/', '')
    regex_seq = '\A{}\Z'.format(y)
    split_indexes = [0]
    index2 = 11
    for index1 in range(len(x)):
        match = re.match(regex_seq, x[index1:index2])
        index2 += 1
        if match:
            split_indexes.append(index1 + split - 1)
        else:
            continue

    return split_indexes


file = str(input('file name: '))
recog_seq = str(input('recognition sequence: '))
recog_seq = recog_seq.replace('N', '.')
genome = get_genome(file)
output = find_rest_indexes(genome, recog_seq)


for i in range(1, len(output)):
    fragment = genome[output[i - 1]:output[i]]
    print('fragment {}, at {} is {} letters long: {}'.format(i, output[i-1], len(fragment), fragment))

last_fragment = genome[output[-1]:len(genome)]
print('fragment {}, at {}, is {} letters long: {}'.format(len(output), output[-1], len(last_fragment), last_fragment))

print('{} fragments total'.format(len(output)))
