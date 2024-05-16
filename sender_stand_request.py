# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests

# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импорт данных запроса из модуля data, в котором определены заголовки, тело запроса и тело набора
import data

# Определение функции post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDERS,
                         json=body)
response = post_new_order(data.orders_body);

# Сохранение номера трека заказа в переменную track_number
track_number = response.json()['track']

print(response.json())
print(track_number)

# Определение функции get_order_track для отправки GET-запроса на получения заказа по его номеру
def get_order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDERS_TRACK + str(track_number))
response = get_order_track(track_number);

print(response.status_code)
