import nltk
nltk.download('wordnet')
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Normalize:
    def __init__(self, sentence):
        self.__tokenize_sentence = word_tokenize(sentence)
        self.__lemmatizer = WordNetLemmatizer()
        self.__norm_commands = (self._remove_stopwords_punct, self._lemmatize_lower)

    def __call__(self, *args, **kwargs):
        tok_sentence = self.__tokenize_sentence
        for norm_com in self.__norm_commands:
            tok_sentence = norm_com(tok_sentence)
        return self._convert_to_str(tok_sentence)

    @staticmethod
    def _convert_to_str(list_words: list):
        return ' '.join(list_words)

    @staticmethod
    def _remove_stopwords_punct(list_words: list):
        return [word for word in list_words if word not in stopwords.words() and word not in string.punctuation]

    def _lemmatize_lower(self, list_words: list):
        return [self.__lemmatizer.lemmatize(word).lower() for word in list_words]
