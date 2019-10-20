import nltk

def DownloadDictionary(dictionaryname):
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download(dictionaryname)

# Tokenize a simple text
sentence = "I want to book a flight from New York to Amsterdam"
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged_tokens = nltk.pos_tag(tokens)

for tokenname, tokentype in tagged_tokens:
    #print(token[0],':',token[1])
    print(tokenname, ':', tokentype)

print()
# Get all verbs of a specific text
textToEvaluate = "After a public divorce, Spider-Man's parents have patched up their differences.The studios behind ""Spider-Man"" have reconciled, with Disney and Sony agreeing to collaborate on a third movie featuring the teenage hero, after a very public split a little over a month ago that caused an uproar among fans.On Friday, the parties announced that Marvel would again have a hand in producing the next sequel, and that Spider-Man would appear in another upcoming Marvel feature.In a statement, Marvel Studios chief Kevin Feige said he is ""thrilled that Spidey's journey in the MCU will continue."""
tokens = nltk.word_tokenize(textToEvaluate)
tagged_tokens = nltk.pos_tag(tokens)
print("All verbs of the text:")
for tokenname, tokentype in [tok for tok in tagged_tokens if tok[1].startswith("VB")]:
    print(tokenname, ':', tokentype)

print()
# Use the sample texts of NLTK
DownloadDictionary("nps_chat")
DownloadDictionary("webtext")

from nltk.book import text1, text2

# Search large texts
text1.concordance("kiss")