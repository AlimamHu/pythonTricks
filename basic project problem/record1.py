import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import numpy as np
freq=44100
duration=5

recording=sd.rec(int(duration*freq), samplerate=freq,channels=2)
t=np.array(recording)
t.shape
print(t.sum())

sd.wait()
write('recording0.wav',freq,recording)
wv.write('recording1.wav',recording,freq, sampwidth=2)
