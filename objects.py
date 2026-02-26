# objects.py

# Tuple to store all valid positions
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

class Player:
    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

class Lineup:
    def __init__(self):
        # Encapsulated private list
        self.__players = []

    def add_player(self, player):
        self.__players.append(player)

    def remove_player(self, number):
        # Subtract 1 because UI shows 1-based index
        return self.__players.pop(number - 1)

    def move_player(self, old_number, new_number):
        player = self.__players.pop(old_number - 1)
        self.__players.insert(new_number - 1, player)

    def get_player(self, number):
        return self.__players[number - 1]

    @property
    def count(self):
        return len(self.__players)

    # Iterator implementation requirement
    def __iter__(self):
        for player in self.__players:
            yield player