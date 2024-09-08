from celery import shared_task
import requests


@shared_task
def send_payment_request(payment_id):
    url = 'https://httpbin.org/post'
    data = {'payment_id': payment_id}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        print('все отработало отлично!!!!!!!!')
    except requests.RequestException as e:
        print(f'Ошибка при отправлении запроса: {e}')
