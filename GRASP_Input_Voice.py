#!/usr/bin/python

from GRASP_Input import GRASP_Input
from time import sleep
import speech_recognition as sr

class GRASP_Input_Voice(GRASP_Input):

    activated = True
    @staticmethod
    def reactivate():
        GRASP_Input_Voice.activated = True

    def received_grip_callback(self, audio):
        try:
            grip = self.recog.recognize_sphinx(audio, language="grasp-cmd")
            print("Sphinx thinks you said " + grip)
            self.queue.put(grip)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

    def setup(self):
        self.recog = sr.Recognizer()
        self.mic = sr.Microphone()
        pass

    def run(self):
        print("Start Voice")
        while(True):
            try:
                if GRASP_Input_Voice.activated:
                    with self.mic as source:
                        self.recog.adjust_for_ambient_noise(source)
                        audio = self.recog.listen(source, timeout= None, phrase_time_limit = 2.0)
                    self.received_grip_callback(audio)
            except KeyboardInterrupt:
                break;

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
        print("Sphinx thinks you said " + r.recognize_sphinx(audio, keyword_entries=[ ('pinch', 1.0), ('ball', 1.0), ('hammer', 1.0) , ('mug', 1.0), ('flat', 1.0), ('rigid', 1.0), ('distance', 1.0)]))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
