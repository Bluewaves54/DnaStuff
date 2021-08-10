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


ipt = str(input('enter dna sequence: '))
dna_seq = list(ipt.upper())
for i in range(0, len(dna_seq)-1):
    if dna_seq[i] == 'T':
        dna_seq[i] = 'U'


protein_seq = []
first_index = 0
end_index = 3
keep_going = True
while first_index < len(dna_seq) and keep_going:
    if list_to_string(dna_seq[first_index:end_index]) in stop_codons:
        # keep_going = False
        protein_seq.append('*')
    for i in acid_letters:
        if list_to_string(dna_seq[first_index:end_index]) in amino_acids[i]:
            protein_seq.append(i)

    first_index += 3
    end_index += 3


print('The protein sequence is', list_to_string(protein_seq))
