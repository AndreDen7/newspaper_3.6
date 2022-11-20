from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError(f'Тип данных{type(value)} нельзя проверить на цензуру')
    list_censor = [
        'хуй', 'хуи', 'хуя', 'блят', 'бляд', 'пизд', 'ебаны', 'ебаная', 'ёбань',
    ]
    for word in list_censor:
        check = (value.lower()).find(word)
        while check != -1:
            len_ = len(word)
            value = value[:check]+'*'*len_ + value[check+len_:]
            check = (value.lower()).find(word)
    return value

