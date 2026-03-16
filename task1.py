def check_age(age: int):
    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'
    return result
