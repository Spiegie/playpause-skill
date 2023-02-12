from mycroft import MycroftSkill, intent_file_handler
from pynput.keyboard import Key, Controller



class Playpause(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.keyboard = Controller

    @intent_file_handler('play.intent')
    def handle_playpause(self, message):
        self.keyboard.tap(Key.media_play_pause)
        self.speak_dialog('play')

    @intent_file_handler('pause.intent')
    def handle_playpause(self, message):
        self.keyboard.tap(Key.media_play_pause)
        self.speak_dialog('pause')


def create_skill():
    return Playpause()

