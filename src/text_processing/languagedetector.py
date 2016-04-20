import langdetect


class LanguageDetector():
    """Implementation using langdetect 1.0.6."""

    def detect(self, text):
        """Returns string of the language id (en, id)
        Override this method in the subclass(es).

        """
        return langdetect.detect(text)

    def detect_languages(self, text):
        """Detect the probabilities for the top languages
        Override this method in the subclass(es).

        """
        return langdetect.detect_langs(text)
