def list_to_string(lst):
    string = ''
    for val in lst:
        string += val
    return string


def multi_line(x):
    num_of_lines = int((len(x)/100)) + 1
    list_x = list(x)
    for i in range(1, num_of_lines):
        list_x.insert(i*100, '\n')

    str_x = list_to_string(list_x)
    return str_x


def find_reverse_compliment(x):
    list_sequence = list(x)
    reverse_compliment = list_sequence[:: -1]

    reversals = {'A': 'T',
                 'T': 'A',
                 'C': 'G',
                 'G': 'C'}

    for i in range(0, len(reverse_compliment)):
        reverse_compliment[i] = reversals[reverse_compliment[i]]

    reverse_compliment = list_to_string(reverse_compliment)
    return reverse_compliment


def find_palindromes(x):
    sequence = list(x.upper())
    end_index = 4
    palindromes = []
    count = 0
    for i in range(0, len(sequence) - 1):
        rc = find_reverse_compliment(sequence[i:end_index])
        original = sequence[i:end_index]
        end_index += 1
        if rc == list_to_string(original):
            palindromes.append(i)
            count += 1

    fp_tuple = (count, palindromes)
    return fp_tuple


def find_protein_seq(x):

    amino_acids = {'F': ['UUU', 'UUC'],
                   'L': ['UUA', 'UUG', 'CUU', 'CUA', 'CUG', 'CUC'],
                   'I': ['AUU', 'AUC', 'AUA'],
                   'M': 'AUG',
                   'V': ['GUU', 'GUC', 'GUA', 'GUG'],
                   'P': ['CCU', 'CCC', 'CCA', 'CCG'],
                   'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                   'A': ['GCU', 'GCC', 'GCA', 'GCG'],
                   'Y': ['UAU', 'UAC'],
                   'H': ['CAU', 'CAC'],
                   'Q': ['CAA', 'CAG'],
                   'N': ['AAU', 'AAC'],
                   'K': ['AAA', 'AAG'],
                   'D': ['GAU', 'GAC'],
                   'E': ['GAA', 'GAG'],
                   'C': ['UGU', 'UGC'],
                   'W': 'UGG',
                   'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                   'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                   'G': ['GGU', 'GGC', 'GGA', 'GGG']}

    stop_codons = ['UAA', 'UAG', 'UGA']
    acid_letters = amino_acids.keys()

    dna_seq = list(x.upper())
    for i in range(0, len(dna_seq) - 1):
        if dna_seq[i] == 'T':
            dna_seq[i] = 'U'

    protein_seq = []
    first_index = 0
    end_index = 3
    keep_going = True
    while first_index < len(dna_seq) and keep_going:
        for i in acid_letters:
            if list_to_string(dna_seq[first_index:end_index]) in amino_acids[i]:
                protein_seq.append(i)
            if list_to_string(dna_seq[first_index:end_index]) in stop_codons:
                keep_going = False

        first_index += 3
        end_index += 3

    return list_to_string(protein_seq)


def find_letter_count(x):
    x = x.upper()
    count_a, count_t, count_c, count_g = 0, 0, 0, 0
    for i in x:
        if i == 'A':
            count_a += 1
        if i == 'T':
            count_t += 1
        if i == 'C':
            count_c += 1
        if i == 'G':
            count_g += 1

    return count_a, count_t, count_c, count_g


dna = str(input('Enter a sequence: '))
fp_return = find_palindromes(dna)
flc_return = find_letter_count(dna)
fps_return = find_protein_seq(dna)
frc_return = find_reverse_compliment(dna)

str_palindromes = ''
for item in fp_return[1][0:len(fp_return[1]) - 2]:
    str_palindromes += str(item)
    str_palindromes += ','

str_palindromes += ' and '
str_palindromes += str(fp_return[1][-1])


print('reverse compliment is ', multi_line(find_reverse_compliment(dna)), '\n')
print('''\n    A occurs''', flc_return[0], '''times
    T occurs''', flc_return[1], '''times
    C occurs''', flc_return[2], '''times
    G occurs''', flc_return[3], 'times\n')
print('there are ', fp_return[0], 'palindromes at ', str_palindromes)
print('The protein sequence is', fps_return, '*')
