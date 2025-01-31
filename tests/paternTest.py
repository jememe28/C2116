import fnmatch

list = ["Сталкер", "Тундра", "Яблоко", "Му", "Юпитер"]
# ? - любой символ
# * - любой символ, в том числе 0 (тоесть работает даже если символ отсутствует, пример снизу)
pattern = 'М?*'

# Поиск по шаблону
result = [item for item in list if fnmatch.fnmatch(item, pattern)]
print(result)