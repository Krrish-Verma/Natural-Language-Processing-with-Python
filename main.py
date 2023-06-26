from nltk.corpus import wordnet as wn

#given a word lemma, synsets() function returns
# list of Synset objects
d = wn.synsets('dog')

print(d) #will print a list of synsets that dog is associated with
