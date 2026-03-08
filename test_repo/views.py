def login_user(request):
    user = request.data.get('user_id')
    return user
