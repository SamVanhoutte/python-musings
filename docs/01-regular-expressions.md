# Regular expressions
This sample contains some interesting (and sometimes complex) challenges that are to be solved by using regular expressions.
Every excercise is implemented as a unit test with tests that should match or must not match.
The comment inside every test describes somewhat what is expected from the regular expression.
Three types of test methods are available:

- `match_regex` : asserts the match of the expression on the value (true/false) is the same as expected
- `get_regex_value` : asserts if the match of the expression on the value (1st matching group) is the same value as expected
- `get_regex_values` : asserts if the matching groups of the expression on the value have the same values as expected