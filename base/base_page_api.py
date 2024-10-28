import requests
import logging
from framework.logger_config import setup_logger
from settings import base_config


class BaseAPI:
    """
        Базовый класс для взаимодействия с API.

        Атрибуты:
        - base_url: str, базовый URL API.
        - logger: logging.Logger, экземпляр логгера для ведения логов.
    """

    def __init__(self):
        """
            Инициализирует объект класса BaseAPI с базовым URL API.
        """
        self.base_url = base_config.base_url_petstore

        # Создает и настраивает логгер для текущего класса, используя имя класса в качестве имени логгера.
        self.logger = setup_logger(self.__class__.__name__)

        # Создает обработчик логирования, который выводит логи в стандартный поток (обычно консоль).
        console_handler = logging.StreamHandler()

        # Устанавливает уровень логирования для консольного обработчика на DEBUG, что означает,
        # что все сообщения уровня DEBUG и выше будут выводиться в консоль.
        console_handler.setLevel(logging.DEBUG)

        # Создает объект форматирования логов, который определяет формат сообщений логов.
        # В данном случае формат включает время записи лог-сообщения, имя логгера, уровень логирования и само сообщение.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Применяет созданный форматтер к консольному обработчику.
        console_handler.setFormatter(formatter)

        # Проверяет, есть ли уже обработчики, присоединенные к логгеру.
        # Если обработчиков нет, добавляет созданный консольный обработчик к логгеру.
        # Это предотвращает добавление нескольких одинаковых обработчиков, если инициализация логгера
        # происходит несколько раз.
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)

    def get(self, endpoint):
        """
            Выполняет GET-запрос к API по-указанному endpoint.

            Параметры:
            - endpoint: str, конечная точка API для выполнения GET-запроса.

            Возвращает:
            - tuple: Кортеж, содержащий JSON-ответ и статус-код.

            Логирование:
            - Информация об успешном ответе.
            - Ошибка, если запрос завершился неудачно.
        """
        try:
            response = requests.get(self.base_url + endpoint)
            response.raise_for_status()

            self.logger.info(f'Успешный ответ {response.status_code}')

            return response.json(), response.status_code

        except requests.exceptions.HTTPError as err:

            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")

            return None, response.status_code

    def post(self, endpoint, data, headers=None, files=None):
        """
            Выполняет POST-запрос к API по-указанному endpoint с передачей данных.

            Параметры:
            - endpoint: str, конечная точка API для выполнения POST-запроса.
            - data: dict, данные для отправки в запросе.
            - headers: dict, заголовки для запроса (по умолчанию None).
            - files: dict, файлы для отправки в запросе (по умолчанию None).

            Возвращает:
            - dict: JSON-ответ от сервера или None, если запрос завершился неудачно.

            Логирование:
            - Информация об успешном ответе.
            - Ошибка, если запрос завершился неудачно.
        """
        try:
            response = requests.post(self.base_url + endpoint, json=data, headers=headers, files=files)
            response.raise_for_status()

            self.logger.info(f'Успешный ответ {response.status_code}')

            return response.json()

        except requests.exceptions.HTTPError as err:

            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")

            return None

    def put(self, endpoint, data):
        """
            Выполняет PUT-запрос к API по-указанному endpoint с передачей данных.

            Параметры:
            - endpoint: str, конечная точка API для выполнения PUT-запроса.
            - data: dict, данные для отправки в запросе.

            Возвращает:
            - dict: JSON-ответ от сервера или None, если запрос завершился неудачно.

            Логирование:
            - Информация об успешном ответе.
            - Ошибка, если запрос завершился неудачно.
        """
        try:
            response = requests.put(self.base_url + endpoint, json=data)
            response.raise_for_status()

            self.logger.info(f'Успешный ответ {response.status_code}')

            return response.json()

        except requests.exceptions.HTTPError as err:

            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")

            return None

    def delete(self, endpoint):
        """
            Выполняет DELETE-запрос к API по-указанному endpoint.

            Параметры:
            - endpoint: str, конечная точка API для выполнения DELETE-запроса.

            Возвращает:
            - dict: JSON-ответ от сервера или None, если запрос завершился неудачно.

            Логирование:
            - Информация об успешном ответе.
            - Ошибка, если запрос завершился неудачно.
        """
        try:
            response = requests.delete(self.base_url + endpoint)
            response.raise_for_status()

            self.logger.info(f'Успешный ответ {response.status_code}')

            return response.json()

        except requests.exceptions.HTTPError as err:

            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")

            return None
