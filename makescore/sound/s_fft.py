import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib as plt


def basic_fft(data,sr):
    time_space = np.shape(data)[0]
    x = np.linspace(0,time_space/sr, time_space)
    y = data
    fft_vals = fft(y)
    freqs = fftfreq(time_space)

    return x, y, freqs, fft_vals