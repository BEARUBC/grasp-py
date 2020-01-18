#!/usr/bin/python


from GRASP_Input import GRASP_Input
from voice_input import VoiceInput


class GRASP_Input_Voice(GRASP_Input):
    activated = True

    def __init__(self, threadID, name, queue):
        super().__init__(threadID, name, queue)
        self.input_processor = VoiceInput()

    @staticmethod
    def reactivate():
        GRASP_Input_Voice.activated = True


    def run(self):
        print("start Voice")
        while True:
            try:
                if GRASP_Input_Voice.activated:
                    user_command = self.input_processor.get_command()
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


# if __name__ == "__main__":
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print('Say something!')
#         audio = r.listen(source)
#     try:
#         print("Sphinx thinks you said " + r.recognize_sphinx(audio, keyword_entries=[('pinch', 1.0), ('ball', 1.0),
#                                                                                      ('hammer', 1.0), ('mug', 1.0),
#                                                                                      ('flat', 1.0)]))
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))
