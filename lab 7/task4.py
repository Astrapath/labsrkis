class fitnesscenter:
    def __init__(self, clientcode, year, month, duration):
        self.clientcode = clientcode
        self.year = year
        self.month = month
        self.duration = duration
    def viewclient(self):
        return (f'Код клиента = {self.clientcode}, год = {self.year}, месяц = {self.month}, '
                f'Продолжительность занятия = {self.duration}\n')
fitnesscenters = [
    fitnesscenter('001', 2025, 1, 21),
    fitnesscenter('002', 2025, 2, 21),
    fitnesscenter('003', 2025, 3, 30),
    fitnesscenter('004', 2025, 4, 21),
    fitnesscenter('005', 2025, 5, 21)
]
longest = fitnesscenters[0]
shortest = fitnesscenters[0]
for session in fitnesscenters:
    if session.duration > longest.duration:
        longest = session
    if session.duration < shortest.duration:
        shortest = session
print(f'Наибольшая сессия: {longest.viewclient()}')
print(f'Наикротчайшая сессия: {shortest.viewclient()}')