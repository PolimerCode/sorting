numbers = [1, 5, 6, 2, 7, 8, 3]
sort_numbers = sorted(numbers)

words = ["cat", "obama", "dog", "obamb", "obamc"]
# wsorted = sorted(words, key=lambda x: x[-1]) # сортировка по букве с конца
wsorted = sorted(words, key=lambda x: (len(x), x)) # сорт по длинне, а затем по алфавиту

# print(wsorted)
# print(sort_numbers)

cities = ["Берлин", "Париж", "Лондон", "Рим", "Амстердам", "Осло"]
sort_cities = sorted(cities, key=lambda x: (len(x), x[-1])) # сорт названий городов по длинне и по последней букве если длина одинакова
print(sort_cities)