from metastablex.regimes.hmm import RegimeHMM
import numpy as np

class RegimeClassifier:

    def __init__(self):
        self.model = RegimeHMM(n_states=3)

    def fit(self, series):

        X = np.array(series).reshape(-1,1)

        self.model.fit(X)

    def predict(self, series):

        X = np.array(series).reshape(-1,1)

        states = self.model.predict(X)

        return states.tolist()
