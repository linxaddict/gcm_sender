import os
from gcm import GCM
from os.path import join, dirname
from dotenv import load_dotenv


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

    response = gcm.json_request(
        registration_ids=registration_ids, data=data,
        collapse_key='push_test', delay_while_idle=True, time_to_live=3600
    )

    if 'success' not in response:
        return False

    topic = 'push_test'

    try:
        gcm.send_topic_message(topic=topic, data=data)
    except IOError:
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
            registration_id = os.environ['REGISTRATION_ID']
            data = {'param1': 'value1', 'param2': 'value2'}

            print('sending push message: {0}'.format(data))
            res = send_push_message(gcm, [registration_id], data)

            print('success: {0}'.format(res))
