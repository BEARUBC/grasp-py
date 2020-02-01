#!/usr/bin/python

from interaction.interaction import Interaction
import speech_recognition as sr


class InteractionVoice(Interaction):
    activated = True

    def __init__(self, thread_id, name, queue):
        super().__init__(thread_id, name, queue)
        self.mic = sr.Microphone()
        self.recog = sr.Recognizer()

    @staticmethod
    def reactivate():
        InteractionVoice.activated = True

    def received_grip_callback(self, user_in):
        try:
            grip = self.recog.recognize_sphinx(user_in, language="grasp-cmd")
            print("Sphinx thinks you said " + grip)
            self.queue.put(grip)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

    def run(self):
        print("start Voice")
        while True:
            try:
                if InteractionVoice.activated:
                    with self.mic as src:
                        self.recog.adjust_for_ambient_noise(src)
                        sound = self.recog.listen(src, timeout=None, phrase_time_limit=2.0)
                    self.received_grip_callback(sound)
            except KeyboardInterrupt:
                break

    @staticmethod
    def deactivate():
        InteractionVoice.activated = False


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
