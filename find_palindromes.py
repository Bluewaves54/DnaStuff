def list_to_string(lst):
    string = ''
    for item in lst:
        string = string + item
    return string


def reverse_compliment(x):
    list_sequence = list(x)

    reverse_compliment = list_sequence[:: -1]

    index = 0
    for i in reverse_compliment:
        if i == 'A':
            reverse_compliment[index] = 'T'
        if i == 'T':
            reverse_compliment[index] = 'A'
        if i == 'G':
            reverse_compliment[index] = 'C'
        if i == 'C':
            reverse_compliment[index] = 'G'

        index += 1

    reverse_compliment = list_to_string(reverse_compliment)

    return reverse_compliment


# dna = str(input("input sequence: "))
# sequence = list(dna)
#
#
# end_index = 4
# palindromes = []
# count = 0
# for i in range(0, len(sequence) - 1):
#     rc = reverse_compliment(sequence[i:end_index])
#     original = sequence[i:end_index]
#     end_index += 1
#     if rc == list_to_string(original):
#         palindromes.append(i)
#         count += 1
#
# str_palindromes = ''
# for item in palindromes[0:len(palindromes) - 2]:
#     str_palindromes += str(item)
#     str_palindromes += ', '
#
# str_palindromes += 'and '
# str_palindromes += str(palindromes[-1])
# print('there are', count, 'palindromes at places', str_palindromes)
# def find_reverse_compliment(x):
#     list_sequence = list(x)
#     reverse_compliment = list_sequence[:: -1]
#
#     reversals = {'A': 'T',
#                  'T': 'A',
#                  'C': 'G',
#                  'G': 'C'}
#
#     for i in range(0, len(reverse_compliment)-1):
#         reverse_compliment[i] = reversals[reverse_compliment[i]]
#
#     reverse_compliment = list_to_string(reverse_compliment)
#     return reverse_compliment
#
#
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

    str_palindromes = ''
    for item in palindromes[0:len(palindromes) - 1]:
        str_palindromes += str(item)
        str_palindromes += ', '

    print('there are', count, 'palindromes at places', str_palindromes, '\n')


find_palindromes('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAACTAATTACTGTCGTTGACAGGACACGAGTAACTCGTCTATCTTCTGCAGGCTGCTTACGGTTTCGTCCGTGTTGCAGCCGATCATCAGCACATCTAGGTTTCGTCCGGGTGTGACCGAAAGGTAAGATGGAGAGCCTTGTCCCTGGTTTCAACGAGAAAACACACGTCCAACTCAGTTTGCCTGTTTTACAGGTTCGCGACGTGCTCGTACGTGGCTTTGGAGACTCCGTGGAGGAGGTCTTATCAGAGGCACGTCAACATCTTAAAGATGGCACTTGTGGCTTAGTAGAAGTTGAAAAAGGCGTTTTGCCTCAACTTGAACAGCCCTATGTGTTCATCAAACGTTCGGATGCTCGAACTGCACCTCATGGTCATGTTATGGTTGAGCTGGTAGCAGAACTCGAAGGCATTCAGTACGGTCGTAGTGGTGAGACACTTGGTGTCCTTGTCCCTCATGTGGGCGAAATACCAGTGGCTTACCGCAAGGTTCTTCTTCGTAAGAACGGTAATAAAGGAGCTGGTGGCCATAGTTACGGCGCCGATCTAAAGTCATTTGACTTAGGCGACGAGCTTGGCACTGATCCTTATGAAGATTTTCAAGAAAACTGGAACACTAAACATAGCAGTGGTGTTACCCGTGAACTCATGCGTGAGCTTAACGGAGGGGCATACACTCGCTATGTCGATAACAACTTCTGTGGCCCTGATGGCTACCCTCTTGAGTGCATTAAAGACCTTCTAGCACGTGCTGGTAAAGCTTCATGCACTTTGTCCGAACAACTGGACTTTATTGACACTAAGAGGGGTGTATACTGCTGCCGTGAACATGAGCATGAAATTGCTTGGTACACGGAACGTTCTGAAAAGAGCTATGAATTGCA')
