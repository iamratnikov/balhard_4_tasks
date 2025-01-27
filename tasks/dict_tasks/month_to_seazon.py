"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию month_to_season, которая принимает номер месяца,
таким образом, чтобы она возвращала название сезона, к которому относится
этот месяц

ПРИМЕРЫ
--------------------------------------------------------------------------------
- month_to_season(12) -> 'Зима'
- month_to_season(4) -> 'Весна'
- month_to_season(7) -> 'Лето'
- month_to_season(9) -> 'Осень'
"""


def month_to_season(month: int) -> str:
    """Возвращает сезон по его номеру

    :param month: номер сезона
    :type month: int

    :return: название сезона, например "зима"
    :rtype: str
    """
    season = {12: "Зима", 4: "Весна", 7: "Лето", 9: "Осень"}.get(month)
    return season


if __name__ == '__main__':
    month_number = int(input('Введите номер месяца: '))
    print(f'Сезон: {month_to_season(month_number)}')
