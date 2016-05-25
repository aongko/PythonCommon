import langdetect
from langdetect.lang_detect_exception import LangDetectException


class LanguageDetector(object):
    """Implementation using langdetect 1.0.6."""

    @staticmethod
    def detect(text):
        """Returns string of the language id (en, id).
        Returns None if exception is caught.
        Override this method in the subclass(es).

        """
        try:
            return langdetect.detect(text)
        except LangDetectException:
            return None

    @staticmethod
    def detect_languages(text):
        """Detect the probabilities for the top languages
        Override this method in the subclass(es).

        """
        try:
            return langdetect.detect_langs(text)
        except LangDetectException:
            return None
