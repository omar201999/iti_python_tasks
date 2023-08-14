def find_letter_indices(sentence, letter):
    indices = []
    for index, char in enumerate(sentence):
        if char == letter:
            indices.append(index)
    return indices


sentence = str(input("Please inter your sentence : ")).lower()
letter_to_find = str(input("Please inter the letter : ")).lower()

indices = find_letter_indices(sentence, letter_to_find)
print(indices)
