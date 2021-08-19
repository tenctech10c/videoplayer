class Invite:
    def __init__(self):
        self._message = "\nDear friends,\nWe have decided to share the first day of\nour new life with our friends and family\nWe request the honour of your presence at\nour wedding\n"
        self._compliment = "\nWith Best Compliment From:\nFriends and Family"
    @property
    def message(self):
        return self._message

    @property
    def compliment(self):
        return self._compliment