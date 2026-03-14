import numpy as np
from metastablex.core.signals import autocorr_lag1
from metastablex.core.potential import potential_landscape

class QWANEngine:

    def __init__(self, series):

        self.series = np.array(series)

        self.returns = np.diff(np.log(self.series+1e-6))

    def resilience(self):

        ac1 = autocorr_lag1(self.returns)

        vol = np.var(self.returns)

        risk = (ac1 + np.log1p(vol))/2

        return 1-risk

    def classify(self):

        r = self.resilience()

        if r > 0.6:
            return "equilibrium"

        elif r > 0.5:
            return "approaching critical"

        elif r > 0.4:
            return "metastable"

        elif r > 0.3:
            return "critical"

        else:
            return "unstable"

    def potential(self):

        return potential_landscape(self.returns)
