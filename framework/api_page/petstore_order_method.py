from base_page_api import BaseAPI


class PetStoreOrder(BaseAPI):

    def create_order_for_pet(self, order_test_data, pet_test_data, status):
        create_order = self.post(endpoint='/v2/store/order',
                                 data={
                                     "id": order_test_data["id"],
                                     "petId": pet_test_data["id"],
                                     "quantity": order_test_data["quantity"],
                                     "shipDate": order_test_data["shipDate"],
                                     "status": status,
                                     "complete": True
                                 })
        return create_order

    def get_find_purchase_order_id(self, id):
        get_find_purchase_order_id = self.get(endpoint=f'/v2/store/order/{id}')
        return get_find_purchase_order_id

    def get_inventories_by_status(self):
        by_status = self.get(endpoint='/v2/store/inventory')
        return by_status

    def order_delete(self, orderId):
        order_delete = self.delete(endpoint=f'/v2/store/order/{orderId}')
        return order_delete
