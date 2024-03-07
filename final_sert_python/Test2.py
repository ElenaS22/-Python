import argparse
import logging
from datetime import datetime

class DateParser:
    def __init__(self, date_text):
        self.date_text = date_text

    def parse(self):
        """
        Разобрать текст и перевести его в дату.
        """
        try:
            # Разбить текст на части
            parts = self.date_text.split()
            day = int(parts[0].rstrip('-й'))  # Извлекаем число дня
            day_name = parts[1]  # Извлекаем название дня недели
            month_name = parts[2]  # Извлекаем название месяца

            # Перевести название месяца в число
            months = {
                'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
                'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
                'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
            }
            month = months[month_name.lower()]

            # Проверить, является ли день числом от 1 до 31
            if day < 1 or day > 31:
                raise ValueError("Некорректное число дня")

            # Создать дату в текущем году
            today = datetime.today()
            year = today.year
            date = datetime(year, month, day)

            # Найти день недели и проверить его совпадение с указанным
            weekdays = {
                'понедельник': 0, 'вторник': 1, 'среда': 2,
                'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6
            }
            expected_weekday = weekdays[day_name.lower()]
            if date.weekday() != expected_weekday:
                raise ValueError("Неверный день недели")

            return date
        except Exception as e:
            logging.error(f"Ошибка при переводе текста '{self.date_text}' в дату: {e}")
            return None

def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description='Перевод текста в дату')
    parser.add_argument('date_text', type=str, help='Текст с датой')
    args = parser.parse_args()

    # Создать экземпляр класса DateParser
    parser = DateParser(args.date_text)

    # Перевести текст в дату используя parse
    date = parser.parse()

    if date:
        print(f"Полученная дата: {date}")
    else:
        print("Ошибка, посмотрите лог для подробностей.")

if __name__ == "__main__":
    main()
