import doctest

class Cat:
    def __init__(self, name: str, age: int, owner: str):
        """
        Создание и подготовка к работе объекта "Кошка".

        :param name: Кличка кошки
        :param age: Возраст кошки
        :param owner: Имя хозяина кошки

        Примеры:
        >>> cat = Cat('Васька', 5, 'Бабушка Тоня')
        """
        if not isinstance(name, str):
            raise TypeError("Кличка кошки должна быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст кошки должен быть типа int")
        if age > 30 or age < 0:
            raise ValueError("Возраст кошки неверен")
        self.age = age

        if not isinstance(owner, str):
            raise TypeError("Имя хозяина кошки должно быть типа str")
        self.owner = owner

    def pet_the_cat(self) -> None:
        """Тискание кошки"""
        ...

    def feed_the_cat(self, food_name: str, food_volume: int) -> None:
        """
        Кормление кошки
        :param food_name: Вид еды
        :param food_volume: Количество еды

        Примеры:
        >>> cat = Cat('Васька', 5, 'Бабушка Тоня')
        >>> cat.feed_the_cat('Вискас', 10)
        """
        if not isinstance(food_name, str):
            raise TypeError("Вид еды должен быть типа str")

        if not isinstance(food_volume, int):
            raise TypeError("Количество еды должно быть типа int")
        if food_volume < 5:
            raise ValueError("Не жадничай")


class UniversityStudent:
    def __init__(self, name: str, status: str, GPA: float):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param status: Статус обучения
        :param GPA: Средний балл

        Пример:
        >>> student = UniversityStudent("Петя Пупкин", "учится", 4.5)
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(status, str):
            raise TypeError("Статус обучения должен быть типа str")
        self.status = status

        if not isinstance(GPA, float):
            raise TypeError("Средний балл должен быть типа float")
        if GPA < 0:
            raise ValueError("Средний балл не может быть отрицательным числом")
        if GPA > 5:
            raise ValueError("Средний балл не может быть больше 5")
        self.GPA = GPA

    def expel_the_student(self) -> str:
        """Отчисление студента

        :return: Новый статус студента

        Пример:
        >>> student = UniversityStudent("Петя Пупкин", "учится", 4.5)
        >>> student.expel_the_student()
        'отчислен'
        """
        self.status = 'отчислен'
        return self.status

    def give_scholarship(self, reason: str, amount_of_money: int):
        """
        Назначение студенту стипендии
        :param reason: Причина назначения стипендии
        :amount_of_money: Размер стипендии

        Пример:
        >>> student = UniversityStudent("Петя Пупкин", "учится", 4.5)
        >>> student.give_scholarship('Учеба на отлично', 5000)
        """
        if self.status == 'отчислен':
            raise ValueError('Нельзя назначить стипендию отчисленному студенту')

        if not isinstance(reason, str):
            raise TypeError("Причина назначения стипендии должна быть типа str")
        self.reason = reason

        if not isinstance(amount_of_money, int):
            raise TypeError("Размер стипендии должен быть типа int")
        self.amount_of_money = amount_of_money

class FoodAtHome:
    def __init__(self, name: str, quantity: int, expiry_date: int):
        """
        Создание и подготовка к работе объекта "Еда дома"

        :param name: Название продукта
        :param quantity: Количество продукта
        :param expiry_date: Через сколько дней продукт испортится. Может быть и отрицательным числом, если продукт уже просрочен.

        Пример:
        >>> product = FoodAtHome('молоко', 1, 6)
        """
        if not isinstance(name, str):
            raise TypeError("Название продукта должно быть типа str")
        self.name = name

        if not isinstance(quantity, int):
            raise TypeError("Количество продукта должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество продукта не может быть отрицательным")
        self.quantity = quantity

        if not isinstance(expiry_date, int):
            raise TypeError("Количество дней, через которое продукт испортится, должно быть типа int")
        self.expiry_date = expiry_date

    def eat_the_food(self) -> None:
        """Съесть еду"""
        ...

    def buy_more_food(self, add_quantity) -> int:
        """Докупить продукты
        :param add_quantity: Количество добавленного продукта

        :return: Сколько продукта есть теперь

        Пример:
        >>> product = FoodAtHome('молоко', 1, 6)
        >>> product.buy_more_food(2)
        3
        """
        if not isinstance(add_quantity, int):
            raise TypeError("Количество добавленного продукта должно быть типа int")
        if add_quantity < 0:
            raise ValueError("Количество добавленного продукта не может быть отрицательным")
        self.add_quantity = add_quantity

        self.quantity += add_quantity
        return self.quantity

if __name__ == "__main__":
    doctest.testmod()
