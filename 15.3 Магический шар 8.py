# 15.3. Магический шар 8 (шар судьбы)

from random import choice

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']


def magic_ball():
    """
    Магический шар (шар судьбы) — шуточный способ предсказывать будущее.
    Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.
    """
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    name = input('Как Вас зовут? ')
    print(f'Привет {name}')

    while True:
        input(f'И так, начнем! Введи вопрос, на который, ты бы хотел получить ответ:\n')
        print(choice(answers))
        next = input(f'{name}, продолжаем? (да/нет)\n')
        if next == 'да':
            continue
        else:
            return 'Возвращайся если возникнут вопросы!'


print(magic_ball())
