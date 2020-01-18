#!/usr/bin/python

import speech_recognition as sr

from GRASP_Input import GRASP_Input


class GRASP_Input_Voice(GRASP_Input):
    activated = True

    @staticmethod
    def reactivate():
        GRASP_Input_Voice.activated = True

    def setup(self):
        self.recog = sr.Recognizer()
        self.mic = sr.Microphone()
        pass

    def recognize_voice(self):
        with self.mic as src:
            self.recog.adjust_for_ambient_noise(src)
            mic_input = self.recog.listen(src, timeout=None, phrase_time_limit=2.0)
            cmd = self.process_voice_command(mic_input)
            if not cmd:
                print("Could not process audio.")
                return False
            return cmd

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

    def run(self):
        print("start Voice")
        while True:
            try:
                if GRASP_Input_Voice.activated:
                    user_command = self.recognize_voice()
                    if not user_command:
                        # No valid command issued, do nothing
                        pass
                    else:
                        self.queue.put(user_command)
            except KeyboardInterrupt:
                break

    @staticmethod
    def deactivate():
        GRASP_Input_Voice.activated = False


if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Say something!')
        audio = r.listen(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio, keyword_entries=[('pinch', 1.0), ('ball', 1.0),
                                                                                     ('hammer', 1.0), ('mug', 1.0),
                                                                                     ('flat', 1.0)]))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
