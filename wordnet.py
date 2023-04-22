from nltk.corpus import wordnet

# Create an empty dictionary to hold the wordnet
wn_dict = {}

# Loop through all synsets in WordNet
for synset in wordnet.all_synsets():
    # Iterate over all lemmas in the synset
    for lemma in synset.lemmas():
        # Get the name of the current lemma and add it as a key to the dictionary if it doesn't already exist
        word = lemma.name()
        if word not in wn_dict:
            wn_dict[word] = []
        # Iterate over all hypernyms (superordinate concepts) and hyponyms (subordinate concepts) of the current lemma
        for hypernym in synset.hypernyms():
            for hypernym_lemma in hypernym.lemmas():
                # Add a relationship between the current word and its hypernyms
                wn_dict[word].append((hypernym_lemma.name(), 'hypernym'))
        for hyponym in synset.hyponyms():
            for hyponym_lemma in hyponym.lemmas():
                # Add a relationship between the current word and its hyponyms
                wn_dict[word].append((hyponym_lemma.name(), 'hyponym'))

# Print the resulting wordnet
for word, relationships in wn_dict.items():
    print(word + ':')
    for related_word, relationship_type in relationships:
        print('\t' + related_word + ' (' + relationship_type + ')')
