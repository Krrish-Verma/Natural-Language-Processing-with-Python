# Natural-Language-Processing-with-Python


# 1. Extracting Dates from a text file
    -Uses dateparser, nltk, and re modules 
    
    
    - 5 different formats of dates are identified: 
            
        1. YYYY-MM-DD 
        2. MM/DD/YYYY
        3. MM/DD/YY
        4. BB DD, YYYY
        5. bb DD, YYYY 
        *bb stands for the full month name or abbreviation of the month (ex: Jul 4, 2023)
    
# 2. Part-of-Speech tagging 
- The text file is first processed and tokenized into sentences and words, as that makes it easier to perform Part-of-Speech tagging. The tagging is then used to find releated synsets for nouns. 
  
- Uses WordNet library to find related synsets for the nouns and saves the processed information into an output file.


   DEPENDENCIES:
- Created with Python 3.10.11
- Requires NLTK (Natural Language Toolkit) library; uses sent_tokenize/word_tokenize and wordnet which is imported from the nltk.corpus.
