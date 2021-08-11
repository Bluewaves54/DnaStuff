def list_to_string(lst):
    string = ''
    for item in lst:
        string = string + item
    return string


def merge(d1, d2):
    return d2.update(d1)


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

file = str(input('file directory: '))
f = open(file).readlines()
f.remove(f[0])
genome = ''
for line in range(0, len(f) - 1):
    genome += f[line].rstrip()


genome = list(genome.upper())
for t in range(0, len(genome) - 1):
    if genome[t] == 'T':
        genome[t] = 'U'


def find_real_protein(x):
    protein_seq = []
    start_index = x
    end_index = x + 3

    while start_index < len(genome):
        if list_to_string(genome[start_index:end_index]) in stop_codons:
            protein_seq.append('*')
        for i in acid_letters:
            if list_to_string(genome[start_index:end_index]) in amino_acids[i]:
                protein_seq.append(i)

        start_index += 3
        end_index += 3

    end_indices, lengths = [], []
    count = 0
    for i in range(0, len(protein_seq) - 1):
        if protein_seq[i] != '*':
            count += 1
        if protein_seq[i] == '*' and count < 100:
            count = 0
        if protein_seq[i] == '*' and count > 100:
            end_indices.append(i)
            lengths.append(count)
            count = 0

    real_proteins = {}
    list_to_string(protein_seq)
    for i in range(0, len(end_indices)):
        pro_start_index = end_indices[i] - lengths[i]
        seq_length = lengths[i]
        pro_end_index = end_indices[i]
        dna_start_index = (pro_start_index * 3 + x)
        dna_stop_index = (pro_end_index * 3 + x)
        p = (list_to_string(protein_seq[pro_start_index:pro_end_index]), '(', str(seq_length),
             ' characters long at ', str(dna_start_index), ', ', str(dna_stop_index), ')')
        protein = ''.join(p)
        real_proteins[dna_start_index] = protein

    return real_proteins


real_proteins_dict = {}
rpd_sorted = sorted(real_proteins_dict)
for start in range(0, 3):
    merge(find_real_protein(start), real_proteins_dict)

rpd_sorted = sorted(real_proteins_dict)

all_real_proteins = ''
for key in rpd_sorted:
    all_real_proteins += (real_proteins_dict[key])
    all_real_proteins += '\n'
print(all_real_proteins)
