from  datetime import datetime
class Task:
    def __init__(self, datestart, datefinish, description):
        self.datestart = datestart
        self.datefinish = datefinish
        self.description = description
tasks = [
    Task('2025-01-01','2025-01-10', 'job1'),
    Task('2025-02-01','2025-03-10', 'job2'),
    Task('2025-03-01','2025-04-10', 'job3'),
    Task('2025-04-01','2025-05-10', 'job4'),
    Task('2025-05-01','2025-06-10', 'job5'),
]
latest = tasks[0]
for task in tasks:
    if datetime.strptime(task.datefinish, '%Y-%m-%d') < datetime.strptime(latest.datestart, '%Y-%m-%d'):
        latest = task
print(f'Start {latest.datestart}, finish {latest.datefinish}, description {latest.description}')