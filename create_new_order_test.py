# Импортируем необходимые библиотеки и модули
import sender_stand_request

import data

# Функция для позитивной проверки
def positive_assert(track_number):
    # В переменную order_response сохраняется результат запроса на получение заказа по его номеру
    order_response = sender_stand_request.get_order_track(track_number)

    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200

# Тест - сценарий создания клиентом заказа и проверка, что по треку заказа можно получить данные о заказе
def test_creat_user_new_order_receive_track_info_order():
    positive_assert(sender_stand_request.track_number)
