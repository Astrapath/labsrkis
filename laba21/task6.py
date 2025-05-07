def season_events(number_of_month):
    month = int(number_of_month)
    if not 1<=month<=12:
        print("Введи реальный номер месяца (1-12): ")
        return
    months = {1:'Январь',2:'Февраль',3:'Март',4:'Апрель',5:'Май',6:'Июнь',7:'Июль',8:'Август',9:'Сентябрь',
          10:'Октябрь',11:'Ноябрь',12:'Декабрь'}
    if 3 <= month <= 5:
        season_desc = "Птицы пели прекрасные песни."
    elif 6 <= month <= 8:
        season_desc = "Солнце светило ярче чем когда-либо."
    elif 9 <= month <= 11:
        season_desc = "Урожай был невероятным."
    else:
        season_desc = "За окном падал белый снег."
    print(f'ВЫ рподелись в {months[month]}, {season_desc}')
season_events(5)
