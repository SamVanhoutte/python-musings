from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.stem import PorterStemmer 
from nltk.tag import untag, str2tuple, tuple2str
from nltk.chunk import tree2conllstr, conllstr2tree, conlltags2tree, tree2conlltags
from nltk.tag.stanford import POSTagger
import nltk

text = "Drive me from Seattle to Brussels"
# Morphology - tagging the words
tokens = word_tokenize(text)
        
# Part of speech tagging
tagged_tokens = pos_tag(tokens)
tagged_tokens = POSTagger(tokens)
# Create named entity tree of tagged tokens
ner_tree = ne_chunk(tagged_tokens)
        
# Get tag structure
iob_tagged = tree2conlltags(ner_tree)
print(iob_tagged)