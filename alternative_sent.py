from nltk.corpus import wordnet

# Get user input
user_input = input('Enter a sentence or phrase: ')

# Tokenize the user input into individual words
words = user_input.split()

# Loop through each word and get its first synonym (if available)
alternatives = []
for word in words:
    synsets = wordnet.synsets(word)
    if synsets:
        synonym = synsets[0].lemmas()[0].name()
        alternatives.append(synonym)
    else:
        alternatives.append(word)

# Join the alternatives back together into a string
alternative_sentence = ' '.join(alternatives)

# Print the resulting sentence with semantic alternatives
print(
    f"The semantic alternative for '{user_input}' is '{alternative_sentence}'.")
