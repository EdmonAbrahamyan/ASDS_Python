from abc import ABC, abstractmethod

class Target(ABC):

    def __init__(self):
        self._adaptee = None

    @abstractmethod
    def request(self):
        pass

    def set_adaptee(self, adaptee):
        self._adaptee = adaptee


class Adapter(Target):
    DICTIONARY = {
        'Hola': 'Hello',
        'Adiós': 'Goodbye'
    }

    def __init__(self, adaptee):
        self.set_adaptee(adaptee)

    def request(self):
        return Adapter.DICTIONARY.get(self._adaptee.speak(), "I don't understand")


class SpanishHello:

    def speak(self):
        return 'Hola'

class SpanishGoodbye:

    def speak(self):
        return 'Adiós'


adapter = Adapter(SpanishHello())
print(adapter.request())

adapter = Adapter(SpanishGoodbye())
print(adapter.request())