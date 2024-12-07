import pyaudio
import numpy as np
import matplotlib.pyplot as pylab
import time

def sound_plot(audio_stream, rotval, i):
    t1 = time.time()
    try:
        data = audio_stream.read(CHUNK, exception_on_overflow=False)
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
        data = b'\x00' * CHUNK  # Handle error or fill with silence
    data_array = np.frombuffer(data, dtype=np.int16)
    pylab.plot(data_array)
    pylab.title(str(i))
    pylab.grid()
    #If the reading is under 32000
    if data[0] < -32000:
        rotval += 1
        if rotval % 2 == 0:
            print('Rotated ' + str(rotval // 2) + ' times.')
    pylab.axis((0, len(data_array), -32768, 32767))
    pylab.savefig("abba.png", dpi=50)
    pylab.close('all')
    return rotval

if __name__ == "__main__":
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2  # Ensure this matches your microphone's capabilities
    RATE = 44100

    p = pyaudio.PyAudio()

    # List and select the input device
    print("Available audio input devices:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            print(f"Device {i}: {info['name']}")

    try:
        device_index = int(input("Select the device index you want to use: "))
    except ValueError:
        print("Invalid input. Using default input device.")
        device_index = None

    # Open the stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=device_index)

    rotval = 0
    try:
        for i in range(int(20 * RATE / CHUNK)):
            rotval = sound_plot(stream, rotval, i)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
