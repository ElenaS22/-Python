import os
import argparse
import logging
from collections import namedtuple

# Создание namedtuple для хранения информации о содержимом директории
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])


def get_directory_content(directory):
    """
    Создать функцию для получения информации о содержимом директории.
    """
    content = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            content.append(FileInfo(name=item, extension='', is_dir=True, parent=directory))
            content.extend(get_directory_content(item_path))
        else:
            name, extension = os.path.splitext(item)
            content.append(FileInfo(name=name, extension=extension, is_dir=False, parent=directory))
    return content


def save_to_log(file_info, log_file):
    """
    Далее функция для сохранения информации в лог-файл.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    for item in file_info:
        if item.is_dir:
            logging.info(f'Directory: {item.name} in {item.parent}')
        else:
            logging.info(f'File: {item.name}, Extension: {item.extension}, Parent Directory: {item.parent}')


def main():
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description='Process directory path')
    parser.add_argument('directory', type=str, help='Path to the directory')
    args = parser.parse_args()

    directory = args.directory

    # Получчить данные о том, что есть в директории
    content = get_directory_content(directory)

    # Сохранить данные в лог-файл
    log_file = 'directory_content.log'
    save_to_log(content, log_file)


if __name__ == "__main__":
    main()
