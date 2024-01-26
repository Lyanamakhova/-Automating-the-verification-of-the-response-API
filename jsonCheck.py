import json

with open('json_example.json', encoding="utf8") as f:
    templates = json.load(f)

def check_int(item):
    return isinstance(item, int)

def check_str(item):
    return isinstance(item, str)

def check_bool(item):
    return isinstance(item, bool)

def check_url(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def check_str_value(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def errorlog(item, value, string):
    error.append({item: f'{value}, {string}'})


error = []

list_of_items = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str',
                 'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str', 'item_price': 'int',
                 'item_url': 'url', 'basket_price': 'str', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
                 'firstInSession': 'bool', 'userAgentName': 'str'}

for items in templates:
    for item in items:
        if item in list_of_items:
            if list_of_items[item] == 'int':
                if not check_int(items[item]):
                    errorlog(item,items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'str':
                if not check_str(items[item]):
                    errorlog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'bool':
                if not check_bool(items[item]):
                    errorlog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'url':
                if not check_url(items[item]):
                    errorlog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'val':
                if not check_str_value(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    errorlog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                errorlog(item, items[item], 'неожиданное значение')
        else:
            errorlog(item, items[item], 'неизвестная переменная')

if error == []:
    print('Pass')
else:
    print('Список ошибок:')
    print(error)
