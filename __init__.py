from mycroft import MycroftSkill, intent_file_handler


class Playpause(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playpause.intent')
    def handle_playpause(self, message):
        self.speak_dialog('playpause')


def create_skill():
    return Playpause()

