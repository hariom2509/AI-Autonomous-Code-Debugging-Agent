from views import login_user


class MockRequest:
    def __init__(self, data):
        self.data = data


def test_login_user():

    request = MockRequest({"user_id": "123"})

    result = login_user(request)

    assert result == "123"