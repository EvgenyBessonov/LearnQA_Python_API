class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase:")
        assert len(phrase) <= 15, "There more than 15 characters in you phrase!"