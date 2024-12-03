class Game:
    def __init__(self, questionBank, round_count):
        self._questionBank = questionBank
        self._players = []
        self._currentPlayer = 0
        self._roundCount = round_count


    def next_round(self):
        """ Move to the next round """
        self._currentPlayer = (self._currentPlayer + 1) % len(self._players) 

    def get_players(self):
        """ Get the list of players in the game """
        return self._players

    def get_round_count(self):
        """ Get the number of rounds in the game """
        return self._roundCount

    def get_state(self):
        """ Print the current state of the game including all players and their scores """
        print("==================================================")
        for i in self._players:
            print(str(i.get_score()) + " - " + i.get_name())

    def add_player(self, player):
        """ Add a player to the game
        Parameters:
            player (Player): The player to be added to the game
        """
        self._players.append(player)
