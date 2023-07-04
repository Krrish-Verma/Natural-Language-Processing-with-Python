################################################################################
#
# FILE: KrrishVerma2.py
# AUTHOR: Krrish Verma
# DESCRIPTION:
#       This code processes a natural language text file, tokenizes it into sentences and words, performs part-of-speech tagging,
#       and extracts nouns. It also uses WordNet to find related synsets for the nouns and saves the processed information into an output file.
#
#
#  DEPENDENCIES:
# Created with Python 3.10.11
# Requires NLTK (Natural Language Toolkit) library; uses sent_tokenize/word_tokenize and wordnet which is imported from the nltk.corpus.
#
################################################################################

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn



def process_text(input_file, output_file):
    try:
        # Read input file
        with open(input_file, 'r') as file:
            text_data = file.read()

        # Split text into paragraphs
        paragraphs = text_data.split("\n")

        with open(output_file, 'w') as file:
            for paragraph in paragraphs:
                # Remove unnecessary tags from paragraphs
                paragraph = paragraph.replace("<p>", "").replace("</p>", "").replace("<h>", "").replace("</h>", "").replace("@", "")

                # Tokenize paragraphs into sentences
                sentences = nltk.sent_tokenize(paragraph)

                for s in sentences:
                    # Tokenize sentence into words and perform part-of-speech tagging
                    words = word_tokenize(s)
                    pos_tagged_words = nltk.pos_tag(words)

                    # Create a tagged sentence string
                    tagged_sentence = " ".join([f"({wrd}, {pos})" for wrd, pos in pos_tagged_words])

                    print("=" * 80)
                    print(s)
                    print(tagged_sentence)

                    # Write sentence and tagged sentence to output file
                    file.write("=" * 80 + '\n')
                    file.write(s+ '\n')
                    file.write(tagged_sentence + '\n')

                    # Extract nouns from tagged words
                    nouns = [wrd for wrd, pos in pos_tagged_words if pos.startswith('NN')]
                    if len(nouns) > 0:
                        # Process the first noun
                        first_noun = nouns[0]
                        first_noun_synsets = wn.synsets(first_noun, pos=wn.NOUN)

                        if len(first_noun_synsets) > 0:
                            file.write("First Noun: {}\n".format(first_noun))
                            file.write("Synsets:\n")




                            for synset in first_noun_synsets:
                                definition = synset.definition()[:30]
                                file.write("\t{} - Definition: {}\n".format(synset, definition))

                                # Process the remaining nouns and find the most related synset
                                for other_noun in nouns[1:]:
                                    other_noun_synsets = wn.synsets(other_noun, pos=wn.NOUN)

                                    if len(other_noun_synsets) > 0:
                                        max_similarity = -1
                                        most_related_synset = None

                                        for other_synset in other_noun_synsets:
                                            similarity = wn.path_similarity(synset, other_synset)

                                            if similarity is not None and similarity > max_similarity:
                                                max_similarity = similarity
                                                most_related_synset = other_synset

                                        if most_related_synset is not None:
                                            definition = most_related_synset.definition()[:30]
                                            file.write("\t\t{} - Related Synset: {} - Definition: {}\n".format(other_noun,  most_related_synset,definition))

                    file.write("=" * 80 + '\n')

        print("Processing complete. Output saved to", output_file)

    except FileNotFoundError:
        print("The input file was not found.")
    except IOError:
        print("An error occurred while processing the file.")





input_file = 'text_web.txt'
output_file = 'output.txt'

process_text(input_file, output_file)
