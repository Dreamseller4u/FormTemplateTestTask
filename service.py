from tinydb import TinyDB, Query
import re

db = TinyDB('db.json')

def get_match(value: str):
    '''
        Валидация входящих значений
        и сравнение с типом.
        Возвращает строковое значение типа
    '''
    valid = {
        'date': r'^\d\d\.\d\d\.\d{4}$',
        'phone': r'^((\+7|7|8)+([0-9]){10})$',
        'email': r'^\S+@\w+.\w{2,4}$',
    }
    if value != '':
        for i, j in valid.items():
            if re.fullmatch(j, value):
                return i
        return 'text'

def find_match(form_values: list):
    '''
        Сравнивает занчения полей из бд
        со значениями полей из формы
        Возвразает шаблон совпадающей формы 
        или если нет совпадений возвращает словарь
        типа {
                f_name1: FIELD_TYPE,
                f_name2: FIELD_TYPE
            }
        где FIELD_TYPE это тип поля, выбранный на основе 
        правил валидации
    '''
    data = db.all()
    d = {}
    for form in data:
        items = [*form.values()][1:]
        if set(items).issubset(form_values):
            return form
    for i in range(len(form_values)):
        if form_values[i] != None:
            d[f'f_name_{i+1}'] = form_values[i]
    return d

def find_match_s(form_values: list):
    '''
        Сравнивает занчения и имена полей из бд
        со значениями полей из формы
        Возвразает шаблон совпадающей формы 
        или если нет совпадений возвращает словарь
        типа {
                f_name1: FIELD_TYPE,
                f_name2: FIELD_TYPE
            }
        где FIELD_TYPE это тип поля, выбранный на основе 
        правил валидации
    '''
    data = db.all()
    for form in data:
        db_names = [*form.keys()][1:]
        db_items = [*form.values()][1:]
        for vals in form_values:
            f_names = [*vals.keys()]
            f_items = [*vals.values()]
            if set(db_items).issubset(f_items) and set(db_names).issubset(f_names):
                return form
    
    return form_values