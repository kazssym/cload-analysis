#!/usr/bin/python

# %%
from matplotlib import pyplot
from scipy.io import wavfile
from numpy import pi, exp, abs, linspace, ones, convolve

# %%
sample_rate, wave = wavfile.read("csave.wav")
time = linspace(0, wave.shape[0] / sample_rate, wave.shape[0])

# %%
pyplot.plot(time[:], wave[:, 0])

# %%
# Complex sinusoids
s0 = exp(2j * pi * 1200 * time)
s1 = exp(2j * pi * 2400 * time)

# %%
window_size = sample_rate / 1200
window = ones(int(window_size)) / window_size

# %%
c0 = abs(convolve(s0[:] * wave[:, 0], window, "same"))
c1 = abs(convolve(s1[:] * wave[:, 0], window, "same"))

# %%
pyplot.plot(time[:], c0[:])
pyplot.plot(time[:], c1[:])

# %%
pyplot.plot(time[:], (c1[:] - c0[:]) / 4096 + 0.5)

# %%

# %%
