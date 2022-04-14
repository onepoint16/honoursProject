from memspectrum import MESA
import numpy as np
import matplotlib.pyplot as plt

N, dt = 10, 1  # Number of samples and sampling interval
no_pred = 2
time = np.arange(0, N) * dt
data = [24, 27, 31, 36, 42, 49, 57, 66, 76, 87]
plt.plot(time[:-1], data[:-1], color = 'k')
plt.show()

M = MESA()
M.solve(data[:-no_pred])
forecast = M.forecast(data[:-no_pred], length = no_pred, number_of_simulations = no_pred*10, 
include_data = False)
median = np.median(forecast, axis = 0) # Ensemble median

plt.plot(time, data, color = 'k')
plt.plot(time[N-no_pred:], data[N-no_pred:], color = 'g', linestyle = '-.', label = 'Observed data')
plt.plot(time[N-no_pred:], median, color = 'r', label = 'median estimate')
plt.show()

# Sum Squared Error just as a quick evaluation
real_values = data[N-no_pred:]
print("Real Values = ", real_values)
print("Median Values = ", median)
SSE = np.sum((real_values - median)**2)
print("SSE = ", SSE)