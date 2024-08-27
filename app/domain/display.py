import abc

from app.domain.quote import Quote

class Display(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def show(self, quote: Quote):
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self):
        raise NotImplementedError
