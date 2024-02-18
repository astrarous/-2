class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        if not isinstance(self.pages, int):
            raise ValueError("Кол-во страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Кол-во страниц должно быть больше 0")

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Кол-во страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

        if not isinstance(self.duration, float):
            raise ValueError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть больше 0")

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. Продолжительность {self.duration} минуты"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


print(Book('Муму', 'И.С. Тургенев'))
print(AudioBook('Муму', 'И.С. Тургенев', 803.4))
print(PaperBook('Муму', 'И.С. Тургенев', 130))
