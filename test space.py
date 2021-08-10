def list_to_string(lst):
    string = ''
    for item in lst:
        string = string + item
    return string


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

f = open('/Users/ayushpal/Library/Mobile Documents/com~apple~TextEdit/Documents/SARS_genome.txt').readlines()
f.remove(f[0])
sars_genome = ''
for i in range(0, len(f) - 1):
    sars_genome += f[i]
start = int(input('what is the starting point? (1, 2, or 3): '))
dna_seq = list(sars_genome.upper())
for i in range(0, len(dna_seq)-1):
    if dna_seq[i] == 'T':
        dna_seq[i] = 'U'


protein_seq = []
index1 = start - 1
end_index = start + 2
keep_going = True
while index1 < len(dna_seq) and keep_going:
    if list_to_string(dna_seq[index1:end_index]) in stop_codons:
        protein_seq.append('*')
    for i in acid_letters:
        if list_to_string(dna_seq[index1:end_index]) in amino_acids[i]:
            protein_seq.append(i)

    index1 += 3
    end_index += 3
stop_codon_indices, lengths = [], []
count = 0
for i in range(0, len(protein_seq) - 1):
    if protein_seq[i] != '*':
        count += 1
    if protein_seq[i] == '*' and count < 100:
        count = 0
    if protein_seq[i] == '*' and count > 100:
        stop_codon_indices.append(i)
        lengths.append(count)
        count = 0


real_proteins = ''
list_to_string(protein_seq)
for i in range(0, len(stop_codon_indices)):
    index1 = stop_codon_indices[i] - lengths[i] - 1
    index2 = stop_codon_indices[i] + 1
    real_proteins += list_to_string(protein_seq[index1:index2])
    real_proteins += '(at '
    real_proteins += str(index1)
    real_proteins += '), '
print('The real protein sequences are', real_proteins)
