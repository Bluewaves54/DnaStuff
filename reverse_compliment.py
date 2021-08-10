def find_palindrome(sequence):
    list_sequence = list(sequence)

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

        index = index + 1

    reverse_compliment = str(reverse_compliment)

    print(reverse_compliment)