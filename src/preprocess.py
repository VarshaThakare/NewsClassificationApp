#Imports

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import nltk
import re

"""
Basic Cleaning Steps:

Remove non eng - sent
Remove url
Remove html tags
Remove email id
Replace - with spaces
Remove stopwords (custom list, include 'th', don't, dont
Remove punctuations (custom punctuations) -> use regex to handle multiple occurences of puncts. as well for eg, ... !!!!! 
Remove numbers
Remove single characters 
Replace multiple spaces with spaces
Lemmatize with POS Tagging
"""
stopwords_custom= ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y']


lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}

def lemmatize_words(text):
    
    pos_tagged_text = nltk.pos_tag(text.split())
    #print(pos_tagged_text)
    
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


def clean_text(sentence):
    sentence = sentence.lower()
    
    sentence = re.sub(r'^https?:\/\/.*[\r\n]*', '', sentence, flags=re.MULTILINE)
    sentence = re.sub(r'<[^>]*>','',sentence)
    sentence = re.sub(r'\S*@\S*\s?','',sentence)
    sentence = re.sub(r'[-]+',' ',sentence)
    sentence = ' '.join([word for word in sentence.split() if word not in stopwords_custom])
    sentence = re.sub(r'[^\w\s]','',sentence)
    sentence = re.sub(r'[^a-z ]+','',sentence)
    sentence = re.sub(r'\\b[a-z]\\b','', sentence)
    sentence = re.sub(r'[\s]+', ' ',sentence)
    sentence = lemmatize_words(sentence)
    
    return sentence


