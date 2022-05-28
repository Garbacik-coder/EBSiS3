import numpy as np
import matplotlib.pyplot as plt

import scipy
from scipy import signal

impulse = signal.unit_impulse(10, 'mid')
shifted_impulse = signal.unit_impulse(7, 2)


# # Sine wave
# t = np.linspace(0, 10, 100)
# amp = 5  # Amplitude
# f = 50
# x = amp * np.sin(2 * np.pi * f * t)
#
# # Exponential Signal
# x_ = amp * np.exp(-t)
#
# plt.figure(figsize=(10, 8))
#
# plt.subplot(2, 2, 1)
# plt.plot(np.arange(-5, 5), impulse, linewidth=3, label='Unit impulse function')
# plt.ylim(-0.01, 1)
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')
#
# plt.subplot(2, 2, 2)
# plt.plot(shifted_impulse, linewidth=3, label='Shifted Unit impulse function')
#
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')
#
# plt.subplot(2, 2, 3)
# plt.plot(t, x, linewidth=3, label='Sine wave')
#
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')
#
# plt.subplot(2, 2, 4)
# plt.plot(t, x_, linewidth=3, label='Exponential Signal')
#
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')
#
# plt.tight_layout()
#
# plt.show()

# ustalenie dziedziny czasu
def create_linspace(timeOfObservation, numberOfSamples):
    return np.linspace(0, timeOfObservation, numberOfSamples)


# utworzenie pojedynczego sygnału
def create_sin_signal(linspace, amplitude, f, phi):
    sig = amplitude * np.sin(2 * np.pi * f * linspace + phi)
    return sig


# utworzenie wykresu sygnału
def print_sin_function(sig, t):
    # plt.subplot(2, 2, 3)
    plt.plot(t, sig, linewidth=3, label='Sine wave')
    plt.xlabel('time.', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.legend(fontsize=10, loc='upper right')
    plt.show()


t = create_linspace(4, 100)
sig1 = create_sin_signal(t, 5, 1, 0)
sig2 = create_sin_signal(t, 5, 1, np.pi/2)

sig3 = (sig1+sig2)
print_sin_function(sig3, t)
