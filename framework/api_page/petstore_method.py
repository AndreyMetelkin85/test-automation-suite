from base_page_api import BaseAPI


class PetStoreUser(BaseAPI):

    def create_user(self, user_test_data, password):
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

    def create_user_with_array(self, user_test_data_1, user_test_data_2, password):
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

    def create_user_with_list(self, user_test_data, password):
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

    def get_user_name(self, user_name):
        get_user_info = self.get(endpoint=f'/v2/user/{user_name}')
        return get_user_info

    def put_user_name(self, user_name, user_test_data, password):
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

    def user_delete(self, user_name):
        user_delete = self.delete(endpoint=f'/v2/user/{user_name}')
        return user_delete
