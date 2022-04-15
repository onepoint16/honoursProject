from memspectrum import MESA

import numpy as np

np.random.seed(0)

def get_forecast(data, pred, sims):
    M = MESA()

    M.solve(data)

    forecast = M.forecast(data, length = pred, number_of_simulations = pred*sims, include_data = False)

    return forecast 