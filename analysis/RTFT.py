import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('/content/sensor_data.csv')
print(df)

time = df.iloc[:, 0]
readings = df.iloc[:, 1]

plt.plot(time,readings)
plt.xlabel("Time (ns)")
plt.ylabel("Signal strength (fsr reading)")
plt.show()
     
# GENERAL ANALYSIS

max_signal = max(readings)
print("Maximum value of FSR reading = ",max_signal)

min_signal = min(readings)
print("Minimum value of FSR reading = ",min_signal)

# FOURIER ANALYSIS


def fourier_transform(time, readings, w_values):
    result = np.zeros_like(w_values, dtype=np.complex)
    dt = time[1] - time[0]
    for i, w in enumerate(w_values):
        integrand = np.exp(-1j * w * time) * readings
        result[i] = np.trapz(integrand, dx=dt)
    return result


# trapz() method is used to compute integration along a specified axis using the composite trapezoidal rule. 
# Here we have used the axis 't'.

w_values = np.linspace(-0,700, 1000)
reading_fourier = fourier_transform(time, readings, w_values)

plt.plot(w_values, reading_fourier.real, label='Real')
# plt.plot(w_values, reading_fourier.imag, label='Imaginary')
plt.title('Fourier Transform of Sensor Readings')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend()
plt.show()


plt.plot(w_values, reading_fourier.imag, label='Imag',c='purple')
plt.title('Fourier Transform of Sensor Readings')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# POWER GENERATED BY THE SIGNAL


power_spectrum = np.abs(reading_fourier) ** 2

# Calculate the total power of the signal
total_power = np.sum(power_spectrum) / len(time)

print("Total power of the signal: {:.2f}".format(total_power))


plt.plot(w_values, power_spectrum, label='Imag',c='purple')
plt.title('Power of Sensor Signals')
plt.xlabel('Frequency')
plt.ylabel('Power in "dw" freq interval')
plt.legend()
plt.show()