import wave as wv
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


#'Distortion Model and Parameter Testing'
#The file is a trial bass recording
filename = 'mellow-bass-guitar-riff_150bpm_A#_major.wav'

hardClip = False  # Set to True for hard clipping, False for soft clipping

distortionAmount = 10.0  # Adjust this value to control the amount of distortion

def distortion(input_signal, amount, size):

    output_signal = np.zeros(size, dtype=float)

    for i in range (0, size):
        x_signalvalue = input_signal[i] * amount

        if x_signalvalue > 1.0:
            y = 1.0 if hardClip else 2.0 / 3.0
        
        elif x_signalvalue <= -1.0:
            y = -1.0 if hardClip else -2.0 / 3.0
        
        else:
            cubedSignal = x_signalvalue * x_signalvalue * x_signalvalue
            y = x_signalvalue if hardClip else x_signalvalue - (cubedSignal / 3)

        output_signal[i] = y
    return output_signal

sample_signal, fs = sf.read(filename)
if sample_signal.ndim > 1:
    sample_signal = sample_signal.mean(axis=1)

outsignal = distortion(sample_signal, distortionAmount, len(sample_signal))
sf.write('distorted_out4.wav', outsignal, fs)







