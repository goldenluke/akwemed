import numpy as np
from metastablex.core.signals import autocorr_lag1
from metastablex.core.signals import skewness
from metastablex.core.signals import kurtosis
from metastablex.core.potential import potential_landscape

class MetastableAnalyzer:

    def __init__(self, series):
        self.series = np.array(series)

    def compute(self):

        returns = np.diff(self.series)

        ac1 = autocorr_lag1(returns)
        vol = np.std(returns)

        skew = skewness(returns)
        kurt = kurtosis(returns)

        centers, potential = potential_landscape(returns)

        risk = (abs(ac1) + vol) / 2

        if risk < 0.2:
            state = "stable"
        elif risk < 0.5:
            state = "metastable"
        else:
            state = "critical"

        return {
            "ac1": float(ac1),
            "volatility": float(vol),
            "skewness": float(skew),
            "kurtosis": float(kurt),
            "state": state
        }
