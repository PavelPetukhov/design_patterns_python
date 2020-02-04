# The command pattern is handy in situations when, for some reason,
# we need to start by preparing what will be executed and then to execute it when needed.filter


class CapitalizeString:
    def __init__(self, string_):
        self._string = string_

    def execute(self):
        self._string = self._string.upper()

    def undo(self):
        self._string = self._string.lower()

        print(self._string)


class History():
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(CapitalizeString('string1'))
history.undo()
