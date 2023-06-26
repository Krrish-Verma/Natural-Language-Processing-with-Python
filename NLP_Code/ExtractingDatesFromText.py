
######################################################################################
#
#           FILE: KrrishVermaAssignment1.py
#
#           AUTHOR: Krrish Verma
#
#           DESCRIPTION:
#                   This program extract dates (5 different formats of it) from a text file by splitting the text into
#                   differnet sentences and utilizes Regular Expression in order to check for different formats.
#
#           DEPENDENCIES:
#           Created with Python 3.10.11 (Python version)
#           Any extra libraries required to run: NLTK, dateparser, re
#
#

####################################################################################
import re
import dateparser
from nltk.tokenize import sent_tokenize




"""
Procedure to extract dates from a given text, which is passed in as a parameter. 
Spaces and periods are removed from the text so that it does not tamper with the formatting of abbriveiations 
of months. 
"""
def extract_dates_from_text(text):
    text = text.replace('.', '')
    text = text.replace(' ', '')
    extracted_dates = [] #stores the extracted dates

    for date_format in date_formats:

        matches = re.findall(date_format, text) # Finds all the matches for the date format in the text
        for match in matches:
            parsed_date = dateparser.parse(match) # Parse the matched date string into a datetime object
            if parsed_date is not None:
                extracted_dates.append(parsed_date)  # Add the parsed date to the list of extracted dates
    return extracted_dates

input_file = open('text_news.txt', 'r')
text_content = input_file.read()

date_formats = [
    r'\d{4}-\d{2}-\d{2}',       # YYYY-MM-DD
    r'\d{2}/\d{2}/\d{4}',       # MM/DD/YYYY
    r'\d{2}/\d{2}/\d{2}',       # MM/DD/YY
    r'\w+ \d{2}, \d{4}',        # BB DD, YYYY
    r'\w{3} \d{2}, \d{4}'       # bb DD, YYYY
]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Add month formats to the list of date formats
for m in months:
    date_formats.append(m + r'\d{1,2},\d{4}')

count = 0

paragraphs = text_content.split('<p>')
for paragraph in paragraphs:
    sentences = sent_tokenize(paragraph) # Tokenize each paragraph into sentences
    for sentence in sentences:
        dates = []  # List to store the formatted dates extracted from the sentence
        extracted_dates = extract_dates_from_text(sentence)
        for date in extracted_dates:
            formatted_date = date.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM-DD' for printing it
            dates.append(formatted_date) # adds the formatted date to the list of dates
        if len(dates) > 0:
            print((sentence, dates))
            count += + 1


#total number of dates
print('\n\n' +  "There were " + str(count) + " dates extracted.")



