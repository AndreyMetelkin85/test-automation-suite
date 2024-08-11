from base.base_page_api import BaseAPI


class PetStoreUser(BaseAPI):
    """
       Класс, представляющий пользователя интернет-магазина домашних животных.

    """

    def create_user(self, user_test_data: dict, password: str):
        """
           Создает нового пользователя в системе и возвращает информацию о нем.

           :param user_test_data - Словарь с данными о пользователе.
           :param password - Пароль пользователя.
        """
        user_info = self.post(endpoint='/v2/user',
                              data={
                                  "id": user_test_data["id"],
                                  "username": user_test_data["username"],
                                  "firstName": user_test_data["firstName"],
                                  "lastName": user_test_data["lastName"],
                                  "email": user_test_data["email"],
                                  "password": password,
                                  "phone": user_test_data["phone"],
                                  "userStatus": user_test_data["userStatus"]
                              })
        return user_info

    def create_user_with_array(self, user_test_data_1: dict, user_test_data_2: dict, password: str):
        """
            Создает новых пользователей в системе с использованием массива данных и возвращает
            информацию о созданных пользователях.

            :param user_test_data_1 - Словарь с данными о пользователе.
            :param user_test_data_2 - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        user_info_with_array = self.post(endpoint='/v2/user/createWithArray',
                                         data=[
                                             {
                                                 "id": user_test_data_1["id"],
                                                 "username": user_test_data_1["username"],
                                                 "firstName": user_test_data_1["firstName"],
                                                 "lastName": user_test_data_1["lastName"],
                                                 "email": user_test_data_1["email"],
                                                 "password": password,
                                                 "phone": user_test_data_1["phone"],
                                                 "userStatus": user_test_data_1["userStatus"]
                                             },
                                             {
                                                 "id": user_test_data_2["id"],
                                                 "username": user_test_data_2["username"],
                                                 "firstName": user_test_data_2["firstName"],
                                                 "lastName": user_test_data_2["lastName"],
                                                 "email": user_test_data_2["email"],
                                                 "password": password,
                                                 "phone": user_test_data_2["phone"],
                                                 "userStatus": user_test_data_2["userStatus"]
                                             }
                                         ])
        return user_info_with_array

    def create_user_with_list(self, user_test_data: dict, password: str):
        """
            Создает нового пользователя в системе с использованием списка данных и возвращает
            информацию о созданном пользователе.

            :param user_test_data - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        user_info_with_list = self.post(endpoint='/v2/user/createWithList',
                                        data=[
                                            {
                                                "id": user_test_data["id"],
                                                "username": user_test_data["username"],
                                                "firstName": user_test_data["firstName"],
                                                "lastName": user_test_data["lastName"],
                                                "email": user_test_data["email"],
                                                "password": password,
                                                "phone": user_test_data["phone"],
                                                "userStatus": user_test_data["userStatus"]
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

    def put_user_name(self, user_name: str, user_test_data: dict, password: str):
        """
           Обновляет информацию о пользователе по его имени пользователя и возвращает обновленную информацию.

            :param user_name - Имя пользователя, для которого требуется обновить информацию.
            :param user_test_data - Словарь с данными о пользователе.
            :param password - Пароль пользователя.
        """
        put_username = self.put(endpoint=f'/v2/user/{user_name}',
                                data={
                                    "id": user_test_data["id"],
                                    "username": user_test_data["username"],
                                    "firstName": user_test_data["firstName"],
                                    "lastName": user_test_data["lastName"],
                                    "email": user_test_data["email"],
                                    "password": password,
                                    "phone": user_test_data["phone"],
                                    "userStatus": user_test_data["userStatus"]
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
