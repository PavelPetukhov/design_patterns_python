import abc

# Given a language, define a representation for its grammar along with an interpreter
# that uses the representation to interpret sentences in the language.


class AbstractExpression(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        self._expression.interpret()


class TerminalExpression(AbstractExpression):

    def interpret(self):
        pass

