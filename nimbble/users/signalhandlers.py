
class FbSignalHandler(object):
    def new_user(self, user):
        fb = user.socialaccount_set.filter(provider='facebook')

        if fb.count() == 0:
            return

        data = fb[0].extra_data
        self.set_picture(user, data)
        self.set_username(user, data)

        user.save()

    def set_picture(self, user, data):
        if 'picture' not in data:
            return

        user.picture_url = data['picture']['data']['url']

    def set_username(self, user, data):
        if 'id' not in data or user.username:
            return

        username = '{}{}'.format(user.first_name.lower(), data['id'])
        user.username = username
