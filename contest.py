# B. Восстановление шифра
#
# n = int(input())
# T = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     T.append(temp)
#
# for i in range(n):
#     for j in range(i+1, n):
#         print(T[i][j])
#
# C = []
import json


class Order:
    def __init__(self, id: int):
        self.id = id
        self.items = {}


class ItemInOrder:
    def __init__(self, id: int, count: int, status: str):
        self.id = id
        self.count = count
        self.status = status


class Event:
    def __init__(self, event_id: int, order_id: int, item_id: int,
                 count: int, return_count: int, status: str):
        self.event_id = event_id
        self.order_id = order_id
        self.item_id = item_id
        self.return_count = return_count
        self.count = count
        self.status = status

    def __str__(self):
        return f"event_id = {self.event_id}"

    @staticmethod
    def create_event(event: dict):
        return Event(event['event_id'], event['order_id'], event['item_id'],
                     event['count'], event['return_count'], event['status'])


def read_file(path: str) -> str:
    input_file = open(path, 'r', encoding='utf8')
    input_json = ""

    for line in input_file:
        input_json += line

    return input_json


def main():
    event_list = list(
        map(Event.create_event, json.loads(read_file('input.txt'))))
    order_dict = {}

    # Ищем, сколько всего было заказов
    event_list.sort(key=lambda event: event.event_id)

    for event in event_list:
        # Если заказа еще нет в словаре
        if event.order_id not in order_dict:
            item = ItemInOrder(event.item_id, event.count -
                               event.return_count, event.status)
            order = Order(event.order_id)
            order.items[item.id] = item
            order_dict[order.id] = order
        # Если данные по заказу уже есть
        else:
            order_dict[event.order_id].items[
                event.item_id].count = event.count - event.return_count
            order_dict[event.order_id].items[
                event.item_id].status = event.status

    orders = []
    # Формируем объект для вывода
    for order_key in order_dict:
        order = {}
        if len(order_dict[order_key].items) != 0:
            items = []
            for item_key in order_dict[order_key].items:
                item = {}
                if order_dict[order_key].items[item_key].count > 0 and \
                        order_dict[order_key].items[
                            item_key].status != "CANCEL":
                    item["id"] = order_dict[order_key].items[item_key].id
                    item["count"] = order_dict[order_key].items[item_key].count
                if len(item) > 0:
                    items.append(item)
            if len(items) > 0:
                order["id"] = order_dict[order_key].id
                order["items"] = items
        if len(order) > 0:
            orders.append(order)

    with open('output.txt', "w", encoding="utf-8") as output_file:
        output_file.write(json.dumps(orders, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()


