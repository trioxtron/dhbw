class Player:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._score = 0


    def get_score(self):
        """ Get the score of the player """
        return self._score

    def get_name(self):
        """ Get the name of the player """
        return self._name

    def add_score(self):
        """ Add a point to the player's score """
        self._score += 1
