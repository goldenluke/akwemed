class ClinicalChat:

    def __init__(self,assistant):

        self.assistant = assistant
        self.history = []

    def ask(self,text):

        result = self.assistant.consult(text)

        self.history.append({
            "input":text,
            "output":result
        })

        return result
