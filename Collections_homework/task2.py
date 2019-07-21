# Ключ-значение :
#   ○ Написать программу, которая берет словарь и меняет местами ключи и значения.
#   Попытаться реализовать за наименьшее кол-во строк.
#     § Пример: {'key1': 'value1', 'key2': 'value2'} -> {'value1': 'key1', 'value2': 'key2'}

# Любой словать с 1 значением в ключе, например:
source_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for k, v in source_dict.items():
    source_dict.pop(k)
    source_dict.update({v: k})
print(source_dict)
