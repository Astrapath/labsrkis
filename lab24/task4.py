import datetime
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август",
          "Сентябрь", "Октябрь", "Ноябоь", "Декабрь"]
def texttodate(text):
    splitd = text.split('.')
    date = datetime.date(int(splitd[2]), int(splitd[1]), int(splitd[0]))
    return f'{weekdays[date.weekday()]}, {date.day} {months[date.month - 1]}, {date.year} год'
textdate = input('Введите дату (ДД.ММ.ГГГГ): ')
print(texttodate(textdate))