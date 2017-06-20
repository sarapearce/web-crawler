
#import pytest

# test the test
# # content of test_sample.py
# def inc(x):
#     return x + 1
#
# def test_answer():
#     assert inc(3) == 5

class spiderTesting(sometestingobjectiimported):


# when given a word with any of these chars, should return word without the chars: INCOMPLETE
def test_cleanword_charset():
    # call in the class, call self for now
    charset = [".", "'", "'s", "Retweet", ",", ":", ";", "?"]
    for char in charset:
        assert self.cleanWord("Test" + char) == "Test"
        assert self.cleanWord("Te" + char + "et") == "Test"

