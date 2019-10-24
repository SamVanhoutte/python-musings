from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conllstr, conllstr2tree, conlltags2tree, tree2conlltags
import nltk

text = "Fly me from Seattle to Brussels"
tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)
ner_tree = ne_chunk(tagged_tokens)
print(ner_tree)        
iob_tagged = tree2conlltags(ner_tree)
print(iob_tagged)