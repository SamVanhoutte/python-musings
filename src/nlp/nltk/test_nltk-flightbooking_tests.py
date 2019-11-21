###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the minimum edit distance
###############################################
import unittest        
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.stem import PorterStemmer 
from nltk.tag import untag, str2tuple, tuple2str
from nltk.chunk import tree2conllstr, conllstr2tree, conlltags2tree, tree2conlltags
 
class FlightChecker(object):
    @staticmethod
    def DetectRoute(text, debugging=False):
        # Morphology - tagging the words
        tokens = word_tokenize(text)
        
        # Part of speech tagging
        tagged_tokens = pos_tag(tokens)

        # Create named entity tree of tagged tokens
        ner_tree = ne_chunk(tagged_tokens)
        #print( ner_tree ) 
        
        # Get tag structure
        # # IoB = inside, outside, beginning - sometimes followed with type of entity
        iob_tagged = tree2conlltags(ner_tree)
        in_chunk = False
        current_chunck = ""
        geo_locations = []
        for word, tag, iob in iob_tagged:
            if(debugging): print(word, "(",tag,"):",":", iob)
            #Detecting if we are in a GeoPolitical chunk
            in_chunk = (iob.startswith("B") or iob.startswith("I")) and (iob.endswith('GPE'))
            if in_chunk:
                current_chunck += word + " "
            if (not(in_chunk) and current_chunck):
                # We just left the chunk as the boolean is false and the chunk has value
                geo_locations.append(current_chunck.strip())
                current_chunck = ""
        
        if(len(geo_locations)==1):
            # Search for the last 'to' word that might be followed by a verb
            last_to_position = max(loc for loc, val in enumerate(iob_tagged) if val[0] == 'to')
            if(len(iob_tagged) > last_to_position):
                # If there is a word following the last to occurance, then take that word as second geo location
                return geo_locations[0], iob_tagged[last_to_position+1][0]
            raise Exception('There are no two geopolitical chunks found', len(geo_locations))
        return geo_locations[0], geo_locations[1]

def DownloadDictionary(dictionaryname):
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download(dictionaryname)

def main():
    DownloadDictionary('maxent_ne_chunker')
    DownloadDictionary('words')
    statement = "I want to make a flight from Seattle to New York."
    source, destination = FlightChecker.DetectRoute(statement, True)
    print(source, ">>", destination)

if __name__ == "__main__": main()

class TestIntents(unittest.TestCase):
    def test_tampa_as_verb(self):
        statement = "I want to book a flight from Seattle to Brussels"
        source, destination = FlightChecker.DetectRoute(statement, True)
        self.assertEqual("Seattle", source)
        self.assertEqual("Brussels", destination)
    def test_easy_one_02(self):
        statement = "I need a plane from Boston to Philadelphia."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertEqual("Boston", source)
        self.assertEqual("Philadelphia", destination)
    def test_combined_name(self):
        statement = "Book me a flight from Washington D.C. to Detroit."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertTrue(source.startswith("Washington"))
        self.assertEqual("Detroit", destination)
    def test_different_formulation(self):
        statement = "I want to book a flight to Atlanta, I’m leaving from Denver."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertEqual("Atlanta", source)
        self.assertEqual("Denver", destination)
        