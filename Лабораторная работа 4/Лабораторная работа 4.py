if __name__ == "__main__":
    class Student:
        """Базовый класс студентов"""

        def __init__(self, name: str, major: str, id_num: int):
            """Создание и подготовка к работе базового класса "Студенты".

            :param name: Имя студента
            :param major: Направление подготовки
            :param id_num: ID студента в системе"""

            self.name = name
            self.major = major
            self._id_num = id_num # ID индивидуален и не может быть изменен в системе

        @property
        def id_num(self):
            return self._id_num

        def __str__(self):
            return f"Студент {self.name}. Направление {self.major}. ID {self._id_num}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, major={self.major!r}, id={self._id_num})"

        def expel(self) -> None:
            """Отчисление студента"""

        def semester_paper(self, paper_name: str) -> str:
            """Курсовая работа

            :param paper_name: Тема курсовой работы
            """
            self.paper_name = paper_name
            return f"Тема курсовой {self.paper_name}"

    class FreshmanStudent(Student):
        """Дочерний класс студентов-первокурсников"""

        def __init__(self, name: str, major: str, id_num: int, passion_for_study: bool):
            """Создание и подготовка к работе дочернего класса "Студенты-первокурсники".

            :param name: Имя студента
            :param major: Направление подготовки
            :param id_num: ID студента в системе
            :param passion_for_study: Любовь к учебе - есть или отсутствует
            """

            super().__init__(name, major, id_num)
            self.passion_for_study = passion_for_study

        def __str__(self):
            return f"Студент {self.name}. Направление {self.major}. ID {self._id_num}. Любовь к учебе {self.passion_for_study}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, major={self.major!r}, id={self._id_num!r}, passion_for_study={self.passion_for_study!r})"

        def semester_paper(self, paper_name: str) -> None:
            """У первокурсников нет курсовых"""
            return None

    print(FreshmanStudent('Иван Иванов', 'Строительство', 7531, True))