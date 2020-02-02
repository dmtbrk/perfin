from perfin.models.users import User


def test_user_set_password(user_data: dict):
    user = User(user_data['username'])
    user.set_password(user_data['password'])

    assert user.username == user_data['username']
    assert user.verify_password(user_data['password'])
