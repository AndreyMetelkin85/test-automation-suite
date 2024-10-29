from base.base_page_api import BaseAPI
from qa_test_data.test_data import TestData


class PetStoreUser(BaseAPI):
    """
       Класс, представляющий пользователя интернет-магазина домашних животных.

    """

    def create_user(self, test_data: TestData, password: str):
        """
           Создает нового пользователя в системе и возвращает информацию о нем.

           :param test_data - Словарь с данными о пользователе.
           :param password - Пароль пользователя.
        """
        user_info = self.post(endpoint='/v2/user',
                              data={
                                  "id": test_data.user.id,
                                  "username": test_data.user.username,
                                  "firstName": test_data.user.firstName,
                                  "lastName": test_data.user.lastName,
                                  "email": test_data.user.email,
                                  "password": password,
                                  "phone": test_data.user.phone,
                                  "userStatus": test_data.user.userStatus
                              })
        return user_info

    def create_user_with_array(self, test_data_1: TestData, test_data_2: TestData, password: str):
        """
            Создает новых пользователей в системе с использованием массива данных и возвращает
            информацию о созданных пользователях.

            :param test_data_1 - Словарь с данными о пользователе.
            :param test_data_2 - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        user_info_with_array = self.post(endpoint='/v2/user/createWithArray',
                                         data=[
                                             {
                                                 "id": test_data_1.user.id,
                                                 "username": test_data_1.user.username,
                                                 "firstName": test_data_1.user.firstName,
                                                 "lastName": test_data_1.user.lastName,
                                                 "email": test_data_1.user.email,
                                                 "password": password,
                                                 "phone": test_data_1.user.phone,
                                                 "userStatus": test_data_1.user.userStatus
                                             },
                                             {
                                                 "id": test_data_2.user.id,
                                                 "username": test_data_2.user.username,
                                                 "firstName": test_data_2.user.firstName,
                                                 "lastName": test_data_2.user.lastName,
                                                 "email": test_data_2.user.email,
                                                 "password": password,
                                                 "phone": test_data_2.user.phone,
                                                 "userStatus": test_data_2.user.userStatus
                                             }
                                         ])
        return user_info_with_array

    def create_user_with_list(self, test_data: TestData, password: str):
        """
            Создает нового пользователя в системе с использованием списка данных и возвращает
            информацию о созданном пользователе.

            :param test_data - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        user_info_with_list = self.post(endpoint='/v2/user/createWithList',
                                        data=[
                                            {
                                                "id": test_data.user.id,
                                                "username": test_data.user.username,
                                                "firstName": test_data.user.firstName,
                                                "lastName": test_data.user.lastName,
                                                "email": test_data.user.email,
                                                "password": password,
                                                "phone": test_data.user.phone,
                                                "userStatus": test_data.user.userStatus
                                            }
                                        ])
        return user_info_with_list

    def get_user_name(self, user_name: str):
        """
            Получает информацию о пользователе по его имени пользователя и возвращает эту информацию.

            :param user_name - Имя пользователя, для которого требуется получить информацию.
        """
        get_user_info = self.get(endpoint=f'/v2/user/{user_name}')
        return get_user_info

    def put_user_name(self, user_name: str, test_data: TestData, password: str):
        """
           Обновляет информацию о пользователе по его имени пользователя и возвращает обновленную информацию.

            :param user_name - Имя пользователя, для которого требуется обновить информацию.
            :param test_data - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        put_username = self.put(endpoint=f'/v2/user/{user_name}',
                                data={
                                    "id": test_data.user.id,
                                    "username": test_data.user.username,
                                    "firstName": test_data.user.firstName,
                                    "lastName": test_data.user.lastName,
                                    "email": test_data.user.email,
                                    "password": password,
                                    "phone": test_data.user.phone,
                                    "userStatus": test_data.user.userStatus
                                })
        return put_username

    def user_delete(self, user_name: str):
        """
            Удаляет пользователя по его имени пользователя и возвращает результат удаления.

            :param user_name - Имя пользователя, которое требуется удалить.
        """
        user_delete = self.delete(endpoint=f'/v2/user/{user_name}')
        return user_delete

    def user_login(self, user_name: str, password: str):
        """
            Выполняет вход пользователя по его имени пользователя и паролю и возвращает результат входа.

            :param user_name - Имя пользователя для входа.
            :param password - Пароль пользователя для входа.
        """
        user_login = self.get(endpoint=f'/v2/user/login?{user_name}{password}')
        return user_login

    def user_log_out(self):
        """
            Выполняет выход текущего пользователя и возвращает результат выхода.
        """
        user_log_out = self.get(endpoint='/v2/user/logout')
        return user_log_out
