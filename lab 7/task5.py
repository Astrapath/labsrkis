class fitnesscenter:
    def __init__(self, clientcode, year, month, duration):
        self.clientcode = clientcode
        self.year = year
        self.month = month
        self.duration = duration
fitnesscenters = [
    fitnesscenter('001', 2022, 1, 21),
    fitnesscenter('002', 2023, 2, 21),
    fitnesscenter('003', 2025, 3, 30),
    fitnesscenter('004', 2025, 4, 21),
    fitnesscenter('005', 2025, 5, 21)
    ]
yearlydur = {}
for i in fitnesscenters:
    if i.year in yearlydur:
        yearlydur[i.year] += i.duration
    else:
        yearlydur[i.year] = i.duration
maxdur = 0
maxyear = 0
for year, duration in yearlydur.items():
    if duration > maxdur:
        maxdur = duration
        maxyear = year
print(f'Год с наибольшей суммарной продолжительностью: {maxyear}, продолжительность: {maxdur}')