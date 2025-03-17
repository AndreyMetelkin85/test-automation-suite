from base.base_page_api import BaseAPI
from qa_test_data.test_data import TestData


class PetStoreOrder(BaseAPI):
    """
        Класс, представляющий операции, связанные с заказами в зоомагазине.

    """

    def create_order_for_pet(self, test_data: TestData, status: str):
        """
            Создать заказ на питомца.

            :param test_data - Словарь с данными о заказе.
            :param status - Статус заказа.
        """
        create_order = self.post(endpoint='/v2/store/order',
                                 data={
                                     "id": test_data.order_data.id,
                                     "petId": test_data.pet_data.id,
                                     "quantity": test_data.order_data.quantity,
                                     "shipDate": test_data.order_data.shipDate,
                                     "status": status,
                                     "complete": True
                                 })
        return create_order

    def get_find_purchase_order_id(self, id: int):
        """
            Получить заказ по его идентификатору.

            :param id - Идентификатор заказа для получения.
        """
        get_find_purchase_order_id = self.get(endpoint=f'/v2/store/order/{id}')
        return get_find_purchase_order_id

    def get_inventories_by_status(self):
        """
            Получить остатки по статусу.
        """
        by_status = self.get(endpoint='/v2/store/inventory')
        return by_status

    def order_delete(self, orderId: int):
        """
            Удалить заказ.

            :param orderId - Идентификатор заказа для удаления.
        """
        order_delete = self.delete(endpoint=f'/v2/store/order/{orderId}')
        return order_delete
