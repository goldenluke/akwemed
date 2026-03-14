from core.rag.search import ClinicalRAG
from core.linguistics.xerente import XerenteInterpreter


class ClinicalAssistant:

    def __init__(self):

        self.rag = ClinicalRAG("data/protocolos.json")
        self.lang = XerenteInterpreter("data/xerente_glossary.json")

    def consult(self, text):

        normalized = self.lang.normalize(text)

        protocol = self.rag.query(normalized)

        title = protocol.get("titulo") or protocol.get("id") or "Protocolo clínico"
        body = protocol.get("texto") or protocol.get("descricao") or str(protocol)

        return {
            "input": text,
            "interpreted": normalized,
            "protocol": title,
            "recommendation": body
        }
