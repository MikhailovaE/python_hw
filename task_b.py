def my_zip(*lists):
  return list(map(lambda *elems: tuple(elems), *lists))

print('Сравнение zip и my_zip (прямое преобразование)')
print(list(zip([1, 2, 2, 3], [9, 8 , 7], ['a', 'b'])))
print(my_zip([1, 2, 2, 3], [9, 8 , 7], ['a', 'b']))

print('\n\nСравнение zip и my_zip (обратное преобразование)')
print(list(zip(*zip([1, 2, 2, 3], [9, 8 , 7], ['a', 'b']))))
print(my_zip(*my_zip([1, 2, 2, 3], [9, 8 , 7], ['a', 'b'])))