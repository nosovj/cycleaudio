import pyaudio
import numpy as np
import pylab
import time


# Plot the audio stream to output png
def sound_plot(audio_stream, rotval):
    t1 = time.time()
    data = np.fromstring(audio_stream.read(CHUNK), dtype=np.int16)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    #If the reading is under 32000
    if data[0] < -32000:
        rotval += 1
        # Since we record it twice when the reading is below we divide it by 2, only print on even numbers
        if rotval % 2 == 0:
            print('Rotated ' + str(rotval/2) + ' times.')
    pylab.axis([0, len(data), -100000, 100000])
    pylab.savefig("abba.png", dpi=50)
    pylab.close('all')
    return rotval


if __name__ == "__main__":
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    rotval = 0
    for i in range(int(20*RATE/CHUNK)):
        rotval = sound_plot(stream, rotval)

    stream.stop_stream()
    stream.close()
    p.terminate()