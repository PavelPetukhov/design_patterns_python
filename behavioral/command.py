import abc

# Command is behavioral design pattern that converts requests or simple operations into objects.

# It adds a level of abstraction between actions and includes an object, which invokes these actions.
# In this design pattern, client creates a command object that includes a list of commands to be executed.
# The command object created implements a specific interface.

# The command pattern is handy in situations when, for some reason,
# we need to start by preparing what will be executed and then to execute it when needed.filter


class Command(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def execute():
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute():
        self._receiver.action()

class Receiver:
    def action(self):
        print('Receiver invoked')


class Invoker:
    def __init__(self):
        self.commands = list()

    def add_command(self, command_):
        self.commands.append(command_)

    def execute(self):
        for command in self.commands:
            command.execute()


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
