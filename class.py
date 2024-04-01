class User():
    def __init__(self, user_id, name):
        self.__user_list = []
        self.id = user_id
        self.name = name

    def get_user_list(self):
        return self.__user_list

    def add_user(self, user_id, name):
        self.__user_list.append({'id': user_id, 'name': name, 'access_level': 'user'})

    def remove_user(self, user_id):
        for user in self.__user_list:
            if user['id'] == user_id:
                self.__user_list.remove(user)
                break


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.access_level = 'admin'
        self.add_user(user_id, name)
        self.update_admin_status()

    def add_user(self, user_id, name):
        super().add_user(user_id, name)

    def remove_user(self, user_id):
        super().remove_user(user_id)

    def update_admin_status(self):
        for user in self.get_user_list():
            if user['id'] == self.id:
                user['access_level'] = 'admin'


admin = Admin(1, 'Александр')
admin.add_user(2, 'Юрий')
admin.add_user(3, 'Алена')
print(admin.get_user_list())

admin.remove_user(2)
print(admin.get_user_list())
