immutable_var = (1, True, "hello")
print(immutable_var)
# immutable_var.append(False) Кортеж является своего рода хранилищем разных данных, которые нельзя изменить.
mutable_list = [1, False, 'bye']
mutable_list.append(True)
mutable_list.extend('hi',)
mutable_list[0] = 'man'
print(mutable_list)

