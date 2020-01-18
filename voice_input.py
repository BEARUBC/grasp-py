import speech_recognition as sr


class VoiceInput:
    def __init__(self, timeout=None):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

        self.mic = sr.Microphone()
        self.recog = sr.Recognizer()

        # timeout in seconds for waiting for a voice command
        self.timeout = timeout
        print(self.mic)

    # Takes in audio, returns the voice command given as text
    def process_voice_command(self, voice):
        try:
            grip = self.recog.recognize_sphinx(voice, language="grasp-cmd")
            print("Sphinx thinks you said " + grip)
            return grip
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        return False

    def get_command(self):
        with self.mic as src:
            self.recog.adjust_for_ambient_noise(src)
            # mic_input = self.recog.listen(src, timeout=self.timeout, phrase_time_limit=2.0)
            print("listening")
            mic_input = self.recog.listen(src, timeout=3)
            return self.recog.recognize_google(mic_input)
            # cmd = self.process_voice_command(mic_input)
            # if not cmd:
            #     print("Could not process audio.")
            #     return False
            # return cmd


if __name__ == "__main__":
    input_processor = VoiceInput()
    while True:
        print(input_processor.get_command())


# if __name__ == "__main__":
#     import pyaudio
#     import wave
#
#     FORMAT = pyaudio.paInt16
#     CHANNELS = 2
#     RATE = 44100
#     CHUNK = 1024
#     RECORD_SECONDS = 5
#     WAVE_OUTPUT_FILENAME = "file.wav"
#
#     audio = pyaudio.PyAudio()
#
#     # start Recording
#     stream = audio.open(format=FORMAT, channels=CHANNELS,
#                         rate=RATE, input=True,
#                         frames_per_buffer=CHUNK)
#     print("recording...")
#     frames = []
#
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     print("finished recording")
#
#     # stop Recording
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#
#     waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#     waveFile.setnchannels(CHANNELS)
#     waveFile.setsampwidth(audio.get_sample_size(FORMAT))
#     waveFile.setframerate(RATE)
#     waveFile.writeframes(b''.join(frames))
#     waveFile.close()


# if __name__ == "__main__":
#     import sounddevice as sd
#     import matplotlib.pyplot as plt
#
#     fs = 44100  # frames per sec
#     sd.default.samplerate = fs
#     sd.default.channels = 2
#
#     duration = 3.0  # Aufnahmezeit
#     recording = sd.rec(int(duration * fs))
#     print("* recording")
#     sd.wait()
#     print("* done!")
#
#     t = [i for i in range(int(duration * fs))]
#
#     plt.plot(t, recording, 'r-')
#     plt.show()
