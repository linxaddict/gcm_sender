TYPE_SHOPPER_FOUND = 0
TYPE_NEW_ORDER_AVAILABLE = 1
TYPE_SHOPPER_VERIFIED = 2


class Shopper:
    KEY_ID = 'id'
    KEY_FIRST_NAME = 'first_name'
    KEY_LAST_NAME = 'last_name'
    KEY_PHOTO = 'photo'

    def __init__(self, shopper_id: int, first_name: str, last_name: str, photo: str):
        super().__init__()

        self.shopper_id = shopper_id
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo

    def as_dict(self) -> dict:
        return {
            self.KEY_ID: self.shopper_id,
            self.KEY_FIRST_NAME: self.KEY_FIRST_NAME,
            self.KEY_LAST_NAME: self.KEY_LAST_NAME,
            self.KEY_PHOTO: self.photo
        }


class NotificationShopperFound:
    KEY_PUSH_TYPE = 'push_type'
    KEY_DELIVERY_DATE = 'delivery_date'
    KEY_SHOPPER = 'shopper'

    def __init__(self, delivery_date: str, shopper: Shopper):
        super().__init__()

        self.notification_type = TYPE_SHOPPER_FOUND
        self.delivery_date = delivery_date
        self.shopper = shopper

    def as_dict(self) -> dict:
        return {
            self.KEY_PUSH_TYPE: self.notification_type,
            self.KEY_DELIVERY_DATE: self.delivery_date,
            self.KEY_SHOPPER: self.shopper.as_dict()
        }


class NotificationNewOrderAvailable:
    KEY_PUSH_TYPE = 'push_type'
    KEY_ORDER_ID = 'order_id'

    def __init__(self, order_id: int):
        self.notification_type = TYPE_NEW_ORDER_AVAILABLE
        self.order_id = order_id

    def as_dict(self) -> dict:
        return {
            self.KEY_PUSH_TYPE: self.notification_type,
            self.KEY_ORDER_ID: self.order_id
        }


class NotificationShopperVerified:
    KEY_PUSH_TYPE = 'push_type'

    def __init__(self):
        super().__init__()
        self.notification_type = TYPE_SHOPPER_VERIFIED

    def as_dict(self) -> dict:
        return {
            self.KEY_PUSH_TYPE: self.notification_type
        }
