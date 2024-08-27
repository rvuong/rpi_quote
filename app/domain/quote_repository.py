import abc

from app.domain.quote import Quote

class QuoteRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self) -> Quote:
        raise NotImplementedError
