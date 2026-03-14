import json


class XerenteInterpreter:

    def __init__(self, glossary_path):

        with open(glossary_path, "r") as f:
            self.glossary = json.load(f)

    def normalize(self, text):

        words = text.lower().split()

        translated = []

        for w in words:

            if w in self.glossary:
                translated.append(self.glossary[w])

            else:
                translated.append(w)

        return " ".join(translated)
