import os
from gcm import GCM
from os.path import join, dirname
from dotenv import load_dotenv
from model import Shopper, NotificationShopperFound, NotificationNewOrderAvailable, NotificationShopperVerified


def create_gcm_client(api_key: str) -> GCM:
    if not api_key:
        return None

    return GCM(os.environ['API_KEY'])


def send_push_message(gcm: GCM, registration_ids: [str], data: dict) -> bool:
    if not gcm:
        return False

    if not registration_ids or not data:
        return False

    response = gcm.json_request(registration_ids=registration_ids, data=data)
    if 'success' not in response:
        return False

    return True

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    if 'REGISTRATION_ID' not in os.environ:
        print('cannot load registration id')
    elif 'API_KEY' not in os.environ:
        print('cannot load api key')
    else:
        gcm = create_gcm_client(os.environ['API_KEY'])
        if not gcm:
            print('cannot create gcm client')
        else:
            shopper = Shopper(1, 'shopper_name', 'shopper_surname', 'http://photo.com/1')
            notification_shopper_found = NotificationShopperFound('2015-10-25T22:34:51+00:00', shopper)
            notification_new_order_available = NotificationNewOrderAvailable(1)
            notification_shopper_verified = NotificationShopperVerified()

            registration_id = os.environ['REGISTRATION_ID']

            print('sending push message: {0}'.format(notification_new_order_available.as_dict()))
            res = send_push_message(gcm, [registration_id], notification_new_order_available.as_dict())

            print('success: {0}'.format(res))
