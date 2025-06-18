class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
users = [
    User('user1', '111111'),
    User('user2', '222222'),
    User('user3', '333333'),
    User('user4', '444444'),
    User('user5', '555555'),

]
def finduser(users):
    login = input('Enter login: ')
    password = input('Enter password: ')
    for user in users:
        if user.login == login and user.password == password:
            return user
    founduser = finduser(users)
    if founduser:
        print(f'Такой пользователь найден: {founduser.login} {founduser.password}')
    else:
        print("Такой не существует")