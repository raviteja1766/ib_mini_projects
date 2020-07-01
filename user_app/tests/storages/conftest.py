import pytest
from user_app.models import User

@pytest.fixture()
def create_users():

    users_list = [
        {
            'username': "username1",
            'password': "Mdjsfs@713"
        },
        {
            'username': "username2",
            'password': "Hksu@761"
        }
    ]
    user_instances_list = []
    users_password_dict = {}
    for user in users_list:
        users_password_dict[user['username']] = user['password']
        user_instances_list.append(
            User(username=user['username'])
        )

    User.objects.bulk_create(user_instances_list)
    user_objs = list(User.objects.all())
    for user in user_objs:
        password = users_password_dict[user.username]
        user.set_password(password)
    User.objects.bulk_update(user_objs, ['password'])