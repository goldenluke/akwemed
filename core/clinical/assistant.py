import numpy as np

from core.linguistics.xerente import XerenteInterpreter
from core.rag.search import ClinicalRAG

from core.metastable.engine import MetastableAnalyzer
from core.metastable.complexity import lempel_ziv


class ClinicalAssistant:

    def __init__(self):

        self.lang = XerenteInterpreter("data/xerente_glossary.json")

        self.rag = ClinicalRAG("data/protocolos.json")

    def consult(self, text):

        normalized = self.lang.normalize(text)

        protocol = self.rag.query(normalized)

        synthetic_signal = np.random.normal(0,1,200)

        analyzer = MetastableAnalyzer(synthetic_signal)

        metastable = analyzer.compute()

        complexity = lempel_ziv(synthetic_signal)

        return {

            "input": text,

            "interpretation": normalized,

            "protocol": protocol.get("titulo","unknown"),

            "recommendation": protocol.get("conduta","avaliar clinicamente"),

            "metastable_state": metastable["state"],

            "volatility": metastable["volatility"],

            "complexity": complexity

        }
