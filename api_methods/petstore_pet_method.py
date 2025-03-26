from base.base_page_api import BaseAPI
from test_data.test_data import TestData
from file.constants import PATH_TO_PHOTO


class PetStorePet(BaseAPI):

    def add_new_pet_store(self, test_data: TestData, status: str):
        """
           Добавляет новое животное в магазин домашних животных.
           :param test_data = Генератор тестовых данных.
           :param status - Статус добавляемого животного.
        """
        add_pet = self.post(endpoint='/v2/pet',
                            data=
                            {
                                "id": test_data.pet_data.id,
                                "category": {
                                    "id": test_data.category.id,
                                    "name": test_data.category.name,
                                },
                                "name": test_data.pet_data.name,
                                "photoUrls": [test_data.pet_data.photoUrls],
                                "tags": [
                                    {
                                        "id": test_data.tags.id,
                                        "name": test_data.tags.name
                                    }
                                ],
                                "status": status
                            })
        return add_pet

    def updates_pet_store(self, test_data: TestData, id: int, status: str):
        """
                Отправляет запрос на обновление информации о питомце на сервере.

                :param test_data - Словарь с данными о животном.
                :param id - Идентификатор питомца.
                :param status - Статус питомца.
        """
        payload = {
            'name': test_data.pet_data.name,
            'status': status
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'

        }
        updates_pet = self.post(endpoint=f'/v2/pet/{id}', data=payload, headers=headers)
        return updates_pet

    def upload_image_pet(self, id: int, metadata: str):
        """
            Метод для загрузки изображения питомца.

            :param id - Идентификатор питомца.
            :param metadata - Дополнительные метаданные для изображения.
        """
        with open(PATH_TO_PHOTO, "rb") as image_file:
            files = [
                ("file", (PATH_TO_PHOTO, image_file, "image/jpeg"))
            ]
            payload = {'additionalMetadata': metadata}
            headers = {
                'Accept': 'application/json'
            }

            upload_image = self.post(endpoint=f'/v2/pet/{id}/uploadImage', files=files, data=payload, headers=headers)
        return upload_image

    def update_an_existing_pet(self, test_data: TestData, status: str):
        """
            Метод для обновления существующего питомца.

            :param test_data - Данные питомца, которые будут использоваться для обновления.
            :param status - Новый статус питомца.
        """
        update_an_existing_pet = self.put(endpoint='/v2/pet',
                                          json=
                                          {
                                              "id": test_data.pet_data.id,
                                              "category": {
                                                  "id": test_data.category.id,
                                                  "name": test_data.category.name,
                                              },
                                              "name": test_data.pet_data.name,
                                              "photoUrls": [
                                                  test_data.pet_data.photoUrls
                                              ],
                                              "tags": [
                                                  {
                                                      "id": test_data.tags.id,
                                                      "name": test_data.tags.name
                                                  }
                                              ],
                                              "status": status
                                          })
        return update_an_existing_pet

    def get_pet_id(self, id: int):
        """
           Метод для получения информации о питомце по его идентификатору.

            :param id - Идентификатор питомца.
        """
        get_pet_id = self.get(endpoint=f'/v2/pet/{id}')
        return get_pet_id

    def get_finds_pets_by_status(self, status: str):
        """
            Получает список домашних животных по указанному статусу.

            :param status - Статус животного, например, "available", "pending" или "sold".
        """
        get_finds_pets = self.get(endpoint=f'/v2/pet/findByStatus?status={status}')
        return get_finds_pets

    def pet_delete(self, id: int):
        """
            Удаляет домашнее животное из магазина по указанному идентификатору.

            :param id - Идентификатор питомца.
        """
        pet_delete = self.delete(endpoint=f'/v2/pet/{id}')
        return pet_delete
