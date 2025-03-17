import requests
from typing import Optional, List, Dict, Tuple, Any
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

    def get(self, endpoint: str, expected_status: Optional[List[int]] = None) -> Tuple[Optional[Dict[str, Any]], int]:
        """
            Выполняет GET-запрос к API по-указанному endpoint.

            :param endpoint: str - конечная точка API для выполнения GET-запроса.
            :param expected_status: Optional[List[int]] - список ожидаемых кодов ответа (по умолчанию 200-299).
            :return: Tuple[Optional[Dict[str, Any]], int] - Кортеж, содержащий JSON-ответ (или None) и статус-код.
        """
        if expected_status is None:
            expected_status = list(range(200, 300))
        try:
            response = requests.get(self.base_url + endpoint)
            response.raise_for_status()

            if response.status_code not in expected_status:
                self.logger.error(f"Неожиданный статус-код: {response.status_code} "
                                  f"(Ожидался один из: {expected_status}). Ответ: {response.text}")
                raise ValueError(f"Получен неожиданный статус-код {response.status_code}")
            self.logger.debug(f'Успешный ответ {response.status_code}')
            return response.json(), response.status_code

        except requests.exceptions.HTTPError as err:
            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")
            return None, response.status_code

    def post(
        self,
        endpoint: str,
        data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict[str, Any]] = None,
        expected_status: Optional[list[int]] = None,
        **kwargs: Any
    ) -> Optional[Dict[str, Any]]:
        """
        Выполняет POST-запрос к API по указанному endpoint с передачей данных.

        :param endpoint: str - конечная точка API.
        :param data: Dict[str, Any] - данные для отправки в запросе.
        :param headers: Optional[Dict[str, str]] - заголовки для запроса (по умолчанию None).
        :param files: Optional[Dict[str, Any]] - файлы для отправки в запросе (по умолчанию None).
        :param expected_status: Optional[list[int]] - ожидаемые коды ответа (по умолчанию 200-299).
        :param kwargs: Дополнительные параметры, передаваемые в requests.post (например, timeout, cookies).
        :return: Optional[Dict[str, Any]] - JSON-ответ от сервера или None, если запрос неудачный.

        Логирование:
        - Информация об успешном ответе.
        - Ошибка, если запрос завершился неудачно.
        """
        if expected_status is None:
            expected_status = list(range(200, 300))

        try:
            response = requests.post(self.base_url + endpoint, json=data, headers=headers, files=files, **kwargs)
            response.raise_for_status()

            if response.status_code not in expected_status:
                self.logger.error(
                    f"Неожиданный статус-код: {response.status_code} "
                    f"(Ожидался один из: {expected_status}). Ответ: {response.text}"
                )
                raise ValueError(f"Получен неожиданный статус-код {response.status_code}")

            self.logger.debug(f'Успешный ответ {response.status_code}')
            return response.json()

        except requests.exceptions.RequestException as err:
            self.logger.error(f"Ошибка запроса: {err}")
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

            self.logger.debug(f'Успешный ответ {response.status_code}')

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

            self.logger.debug(f'Успешный ответ {response.status_code}')

            return response.json()

        except requests.exceptions.HTTPError as err:

            self.logger.error(f"HTTP Error: {err} - Статус-код: {response.status_code}")

            return None
