
class Model:

    def load(self):
        raise NotImplementedError

    def store(self):
        raise NotImplementedError


class User(Model):
    pass

class Game(Model):
    pass
