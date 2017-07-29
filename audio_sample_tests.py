import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 60
WAVE_OUTPUT_FILENAME = 'test.wav'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print('- Recording ' + WAVE_OUTPUT_FILENAME + ' for: ' + str(RECORD_SECONDS) + ' seconds...')

# Frame holder
f = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    f.append(data)

print('- Finished ' + WAVE_OUTPUT_FILENAME)

stream.stop_stream()
stream.close()
p.terminate()

wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(p.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(f))
wave_file.close()