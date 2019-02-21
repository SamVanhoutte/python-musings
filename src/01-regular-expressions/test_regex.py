import unittest                     # unit testing ftw
import re                           # regular expressions

# class RegexTester:
#     @staticmethod
#     def match_regex(testCase, expression, valueToMatch, shouldMatch):
#         regEx = re.compile(expression)
#         testCase.assertEqual(shouldMatch, regEx.match(valueToMatch))


class RegexTestMethods(unittest.TestCase):
    def test_excercise_01(self):
        # match three characters followed by .
        expression = r'.{3}\.'
        self.match_regex(expression, r'cat.', True)
        self.match_regex(expression, r'896.', True)
        self.match_regex(expression, r'?=+.', True)
        self.match_regex(expression, r'abc1', False)
    
    def test_excercise_02(self):
        # Matching words starting with c, m or f followed by ‘an
        expression = r'(c|m|f)an'
        self.match_regex(expression, r'can', True)
        self.match_regex(expression, r'man', True)
        self.match_regex(expression, r'fan', True)
        self.match_regex(expression, r'dan', False)
        self.match_regex(expression, r'ran', False)
        self.match_regex(expression, r'pan', False)

    def test_excercise_03(self):
        #Matching three letters Words ending in “og”, not starting with a “b”
        expression = r'[^b]og'
        self.match_regex(expression, r'hog', True)
        self.match_regex(expression, r'dog', True)
        self.match_regex(expression, r'bog', False)

    def test_excercise_04_1(self):
        # Method one
        # Matching three letter words starting with an uppercase letter (use three different methods)
        expression = r'[A-Z][a-zA-Z]{2}'
        self.match_regex(expression, r'Ana', True)
        self.match_regex(expression, r'Bob', True)
        self.match_regex(expression, r'Cpc', True)
        self.match_regex(expression, r'aax', False)
        self.match_regex(expression, r'bby', False)
        self.match_regex(expression, r'ccz', False)

    def test_excercise_04_2(self):
        # Method two
        # Matching three letter words starting with an uppercase letter (use three different methods)
        expression = r'[A-Z]..'
        self.match_regex(expression, r'Ana', True)
        self.match_regex(expression, r'Bob', True)
        self.match_regex(expression, r'Cpc', True)
        self.match_regex(expression, r'aax', False)
        self.match_regex(expression, r'bby', False)
        self.match_regex(expression, r'ccz', False)

    def test_excercise_04_3(self):
        # Method three
        # Matching three letter words starting with an uppercase letter (use three different methods)
        expression = r'[A-Z][a-zA-Z][a-zA-Z]'
        self.match_regex(expression, r'Ana', True)
        self.match_regex(expression, r'Bob', True)
        self.match_regex(expression, r'Cpc', True)
        self.match_regex(expression, r'aax', False)
        self.match_regex(expression, r'bby', False)
        self.match_regex(expression, r'ccz', False)

    def test_excercise_05(self):
        #Matching wazzzzup as long as it has more than one z
        expression = r'waz{2,}up'
        self.match_regex(expression, r'wazzzzzup', True)
        self.match_regex(expression, r'wazzzup', True)
        self.match_regex(expression, r'wazup', False)
        self.match_regex(expression, r'aax', False)

    def test_excercise_06(self):
        # Matching 2 to 4 a’s followed by 0 to 4 b’s and 1 to 2 c’s
        expression = r'a{2,4}b{0,4}c{1,2}'
        self.match_regex(expression, r'aaaabcc', True)
        self.match_regex(expression, r'aabbbbc', True)
        self.match_regex(expression, r'aacc', True)
        self.match_regex(expression, r'a', False)

    def test_excercise_07(self):
        # Matching a number followed by “file found?” or “files found?” – use the question mark operator
        expression = r'\d+ files? found\?'
        self.match_regex(expression, r'1 file found?', True)
        self.match_regex(expression, r'2 files found?', True)
        self.match_regex(expression, r'24 files found?', True)
        self.match_regex(expression, r'No files found', False)

    def test_excercise_08(self):
        # Matching a number followed by “file found?” or “files found?” – use the question mark operator
        expression = r'\d+ files? found\?'
        self.match_regex(expression, r'1 file found?', True)
        self.match_regex(expression, r'2 files found?', True)
        self.match_regex(expression, r'24 files found?', True)
        self.match_regex(expression, r'No files found', False)

    def test_excercise_09(self):
        # Matching a number followed by a dot, some whitespace and the text “abc”
        expression = r'\d+.\s+abc'
        self.match_regex(expression, r'1.  abc', True)
        self.match_regex(expression, r'2.   abc', True)
        self.match_regex(expression, r'332.           abc', True)
        self.match_regex(expression, r'4.abc', False)

    def test_excercise_10(self):
        # Matching the word mission followed by a ‘: ’ but only in the beginning of a string
        expression = r'^[M|m]ission: '
        self.match_regex(expression, r'Mission: successful', True)
        self.match_regex(expression, r'Last Mission: unsuccessful', False)
        self.match_regex(expression, r'Next Mission: successful upon capture of target', False)

    def test_excercise_11(self):
        # Matching “I love “ followed by “cats” or “dogs”
        expression = r'I love (cats|dogs)'
        self.match_regex(expression, r'I love dogs', True)
        self.match_regex(expression, r'I love cats', True)
        self.match_regex(expression, r'I love cogs', False)
        self.match_regex(expression, r'I love logs', False)

    def test_excercise_12(self):
        # Matching a date (three letter month, 4 digit year), eliminating whitespace, catching the full date, and the year (hint, nested sub-groups)
        expression = r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d\d\d\d)'
        # Not sure about the nest sub groups ?
        self.get_regex_value(expression, r'    Jan 1987', 'Jan 1987')
        self.get_regex_value(expression, r'  May 1969   ', 'May 1969')
        self.get_regex_value(expression, r'Aug 2011       ', 'Aug 2011')

    def test_excercise_13(self):
        # Matching .pdf files and capturing their name (without path!)
        # Using two groups and the non-capturing (?:) syntax
        expression = r'(.*)(?:.pdf(\s|$))'
        self.get_regex_value(expression, r'file_record_transcript.pdf', 'file_record_transcript')
        self.get_regex_value(expression, r'file_07241999.pdf', 'file_07241999')
        self.get_regex_value(expression, r'testfile_fake.pdf.tmp', None)

    def test_excercise_14(self):
        # Matching Numbers
        # First allow optional use of + or - sign
        # Then require digits, optionally with zero or one decimal/thousand seperators
        # After the seperator, allow e sign and require string to end with digit
        expression = r'^(-|\+)?\d+(.|,)?\d+(\.\d+)?\d*e?\d*$'
        self.match_regex(expression, r'3.14529', True)
        self.match_regex(expression, r'-255.34', True)
        self.match_regex(expression, r'129', True)
        self.match_regex(expression, r'1.9e10', True)
        self.match_regex(expression, r'123,340.00', True)
        self.match_regex(expression, r'.123,340', False)
        self.match_regex(expression, r'123,340.', False)
        self.match_regex(expression, r'123,,340.00', False)
        self.match_regex(expression, r'720p', False)

    def test_excercise_15(self):
        # Matching phone numbers
        expression = r'(\d{3})'
        self.get_regex_value(expression, r'415-555-1234', '415')
        self.get_regex_value(expression, r'650-555-2345', '650')
        self.get_regex_value(expression, r'(416)555-3456', '416')
        self.get_regex_value(expression, r'202 555 4567', '202')
        self.get_regex_value(expression, r'4035555678', '403')
        self.get_regex_value(expression, r'1 416 555 9292', '416')

    def test_excercise_16(self):
        # Matching eMails
        # The first 'non greedy' part is important, to force the split at the optional + character
        # Also making sure the domain name is at least 2 chars and contains a dot, followed by other characters
        expression = r'(.+?)(?:(\+.*))*(?:@)((?:[a-zA-Z]{2,})(?:.))+'
        self.get_regex_value(expression, r'tom@hogwarts.com', 'tom')
        self.get_regex_value(expression, r'tom.riddle@hogwarts.com', 'tom.riddle')
        self.get_regex_value(expression, r'tom.riddle+regexone@hogwarts.com', 'tom.riddle')
        self.get_regex_value(expression, r'tom@hogwarts.eu.com', 'tom')
        self.get_regex_value(expression, r'potter@hogwarts.com', 'potter')
        self.get_regex_value(expression, r'harry@hogwarts.com', 'harry')
        self.get_regex_value(expression, r'hermione+regexone@hogwarts.com', 'hermione')

    def test_excercise_17(self):
        # Capturing HTML
        expression = r'^(?:<)([\w]+)(?:.*>)'
        self.get_regex_value(expression, r'<a>This is a link</a>', 'a')
        self.get_regex_value(expression, r'<a href=\'https://regexone.com\'>Link</a>', 'a')
        self.get_regex_value(expression, r'<div class=\'test_style\'>Test</div>', 'div')
        self.get_regex_value(expression, r'<div>Hello <span>world</span></div>', 'div')

    def test_excercise_18(self):
        # Matching image files
        expression = r'(.+)(?:\.(jpe?g|gif|png)(\s|$))'
        self.get_regex_value(expression, r'.bash_profile', None)
        self.get_regex_value(expression, r'workspace.doc', None)
        self.get_regex_values(expression, r'img0912.jpg', ['img0912', 'jpg'])
        self.get_regex_values(expression, r'updated_img0914.jpeg', ['updated_img0914', 'jpeg'])
        self.get_regex_value(expression, r'documentation.html', None)
        self.get_regex_values(expression, r'favicon.gif', ['favicon', 'gif'])
        self.get_regex_value(expression, r'img0913.jpg.tmp', None)

    def test_excercise_19(self):
        # Trimming whitespace from start and end of lines
        expression = r'(?:^\s*)(.*?)(?:\s*$)'
        self.get_regex_value(expression, r'   The quick brown fox...', 'The quick brown fox...')
        self.get_regex_value(expression, r'Jumps over the lazy dog      ', 'Jumps over the lazy dog')


    def test_excercise_20(self):
        # Extracting information from a log file
        expression = r'(?:.*)(?:at widget.List.)(.*)\((.*):(\d+)\)'
        self.get_regex_values(expression, r'W/dalvikvm( 1553): threadid=1: uncaught exception', None)
        self.get_regex_values(expression, r'E/( 1553): FATAL EXCEPTION: main', None)
        self.get_regex_values(expression, r'E/( 1553): java.lang.StringIndexOutOfBoundsException', None)
        self.get_regex_values(expression, r'E/( 1553):   at widget.List.makeView(ListView.java:1727)', ['makeView', 'ListView.java', '1727'])
        self.get_regex_values(expression, r'E/( 1553):   at widget.List.fillDown(ListView.java:652)', ['fillDown', 'ListView.java', '652'])
        self.get_regex_values(expression, r'E/( 1553):   at widget.List.fillFrom(ListView.java:709)', ['fillFrom', 'ListView.java', '709'])

    def test_excercise_21(self):
        # URI Parsing
        expression = r'([a-zA-Z]+)(?::\/\/)(.+?)(?::)?(\d*)(?:\/)'
        self.get_regex_values(expression, r'ftp://file_server.com:21/top_secret/life_changing_plans.pdf', ['ftp', 'file_server.com', '21'])
        self.get_regex_values(expression, r'https://regexone.com/lesson/introduction#section', ['https', 'regexone.com'])
        self.get_regex_values(expression, r'file://localhost:4040/zip_file', ['file', 'localhost', '4040'])
        self.get_regex_values(expression, r'market://search/angry%20birds', ['market', 'search'])
        self.get_regex_values(expression, r'https://s3cur3-server.com:9999/', ['https', 's3cur3-server.com', '9999'])

    def test_excercise_22(self):
        # Detecting the end of a sentence
        expression = r'^(-|\+)?\d+(.|,)?\d+(\.\d+)?\d*e?\d*$'
        self.match_regex(expression, r'assumes word senses. Within', True)
        self.match_regex(expression, r'does the clustering. In the', True)
        self.match_regex(expression, r'but when? It was hard to tel', True)
        self.match_regex(expression, r'he arrive." After she had', True)
        self.match_regex(expression, r'mess! He did not let it', True)
        self.match_regex(expression, r't wasn\'t hers!\' She replied', True)
        self.match_regex(expression, r'always thought so.) Then', True)
        self.match_regex(expression, r'in the U.S.A., people often', False)
        self.match_regex(expression, r'John?", he often thought, but', False)
        self.match_regex(expression, r'weighed 17.5 grams', False)
        self.match_regex(expression, r'well ... they\'d better not', False)
        self.match_regex(expression, r'A.I. has long been a very', False)
        self.match_regex(expression, r'like that", he thought', False)
        self.match_regex(expression, r'but W. G. Grace never had much', False)

    def test_excercise_23(self):
        # What does the reg-exp match
        expression = r'\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?'
        self.match_regex(expression, r'assumes word senses. Within', True)
        self.match_regex(expression, r'does the clustering. In the', False)

    def match_regex(self, expression, valueToMatch, shouldMatch):
        # Asserts if the expression matches (or not) for the value
        regEx = re.compile(expression)
        match = bool(regEx.search(valueToMatch))
        self.assertEqual(shouldMatch, match, 'value ' + valueToMatch + ' failed the test')


    def get_regex_value(self, expression, valueToMatch, expectedValue):
        regEx = re.compile(expression)
        searchResult = regEx.search(valueToMatch)
        print(searchResult)
        if expectedValue == None:
            self.assertIsNone(searchResult, 'The search result should be empty')
        else:
            self.assertIsNotNone(searchResult, 'The search result was empty')
            # check the 1st group (group() and group(0) get all values)
            self.assertEqual(expectedValue, searchResult.group(1))  

    def get_regex_values(self, expression, valueToMatch, expectedValues):
        regEx = re.compile(expression)
        searchResult = regEx.search(valueToMatch)
        print(searchResult)
        if expectedValues == None:
            self.assertIsNone(searchResult, 'The search result should be empty')
        else:
            idx = 1
            for expectedValue in expectedValues:
                self.assertIsNotNone(searchResult, 'The search result was empty')
                # check the 1st group (group() and group(0) get all values)
                self.assertEqual(expectedValue, searchResult.group(idx)) 
                idx += 1 


# (.*)(?:\.|\?|!)

#     assumes word senses. Within
# does the clustering. In the
# but when? It was hard to tel
# he arrive." After she had
# mess! He did not let it
# t wasn't hers!' She replied
# always thought so.) Then
# in the U.S.A., people often
# John?", he often thought, but
# weighed 17.5 grams
# well ... they'd better not
# A.I. has long been a very
# like that", he thought
# but W. G. Grace never had much 