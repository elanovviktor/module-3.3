def  print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params('1:')# здесь мы обозначили 1 элемент, омьальные б и с происутствуют по умолчанию
print_params()# распакавали пустыми скобками, соответственно получиди значения (а,б, с)
print_params(b=25)# изменили значение б
print_params(c=[1, 2, 3])
#Распаковка параметров
# распаковка
print()
print('2:')
values_list = ('hanter', 741, True)# создали список
print_params(*values_list)# сделали изменяемый обьект
values_dict = {'a': 'text', 'b': False, 'c': 77}# cловарь с тремя клячами?????
print_params(**values_dict)# теперь в функции парамс должны быть 2 параметра с одной и двумя*
#Распаковка + отдельные параметры:
print()
print('3:')
values_list_2 = [74.63, 'string']
print_params(*values_list_2,42)




