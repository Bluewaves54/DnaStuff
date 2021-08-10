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
    sars_genome += f[i].rstrip()


start = int(input('what is the starting point? (1, 2, or 3): '))
sars_genome = list(sars_genome.upper())
for i in range(0, len(sars_genome) - 1):
    if sars_genome[i] == 'T':
        sars_genome[i] = 'U'


protein_seq = []
start_index = start - 1
end_index = start + 2
# keep_going = True
while start_index < len(sars_genome):
    if list_to_string(sars_genome[start_index:end_index]) in stop_codons:
        protein_seq.append('*')
    for i in acid_letters:
        if list_to_string(sars_genome[start_index:end_index]) in amino_acids[i]:
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


real_proteins = ''
list_to_string(protein_seq)
for i in range(0, len(end_indices)):
    pro_start_index = end_indices[i] - lengths[i]
    seq_length = lengths[i]
    pro_end_index = end_indices[i]
    dna_start_index = (pro_start_index * 3 + start - 1)
    dna_stop_index = (pro_end_index * 3 + start - 1)
    real_proteins += list_to_string(protein_seq[pro_start_index:pro_end_index])
    real_proteins += '(at '
    real_proteins += str(dna_start_index)
    real_proteins += ', '
    real_proteins += str(dna_stop_index)
    real_proteins += '), \n'
    print(dna_start_index, dna_stop_index, seq_length)


print('The real protein sequences are\n', real_proteins.lstrip())

print(sars_genome[21549:21552])
