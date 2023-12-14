from difflib import SequenceMatcher


class Matcher(SequenceMatcher):

    def match(self):
        return True if self.ratio() >= 0.8 else False
