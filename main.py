# main.py
import db
import ui
from objects import Player, Lineup, POSITIONS

def load_lineup():
    """Loads raw data from DB layer into Business objects."""
    lineup = Lineup()
    raw_players = db.read_players()
    for p in raw_players:
        player = Player(p['first_name'], p['last_name'], p['position'], p['at_bats'], p['hits'])
        lineup.add_player(player)
    return lineup

def save_lineup(lineup):
    """Converts Business objects back to primitive dicts for the DB layer."""
    players_list = []
    for player in lineup:
        players_list.append({
            "first_name": player.first_name,
            "last_name": player.last_name,
            "position": player.position,
            "at_bats": player.at_bats,
            "hits": player.hits
        })
    db.write_players(players_list)

def add_player(lineup):
    first = input("First name: ")
    last = input("Last name: ")
    pos = ui.get_position("Position: ", POSITIONS)
    ab = ui.get_int("At bats: ", 0, 10000)
    
    # Validation: Cannot have more hits than at-bats
    hits = ui.get_int("Hits: ", 0, ab)
    
    player = Player(first, last, pos, ab, hits)
    lineup.add_player(player)
    save_lineup(lineup)
    print(f"{player.full_name} was added.\n")

def remove_player(lineup):
    number = ui.get_int("Number: ", 1, lineup.count)
    player = lineup.remove_player(number)
    save_lineup(lineup)
    print(f"{player.full_name} was deleted.\n")

def move_player(lineup):
    old_num = ui.get_int("Current lineup number: ", 1, lineup.count)
    player = lineup.get_player(old_num)
    print(f"{player.full_name} was selected.")
    new_num = ui.get_int("New lineup number: ", 1, lineup.count)
    
    lineup.move_player(old_num, new_num)
    save_lineup(lineup)
    print(f"{player.full_name} was moved.\n")

def edit_position(lineup):
    number = ui.get_int("Lineup number: ", 1, lineup.count)
    player = lineup.get_player(number)
    print(f"You selected {player.full_name} POS={player.position}")
    
    new_pos = ui.get_position("New position: ", POSITIONS)
    player.position = new_pos
    save_lineup(lineup)
    print(f"{player.full_name} was updated.\n")

def edit_stats(lineup):
    number = ui.get_int("Lineup number: ", 1, lineup.count)
    player = lineup.get_player(number)
    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")
    
    ab = ui.get_int("At bats: ", 0, 10000)
    hits = ui.get_int("Hits: ", 0, ab)
    
    player.at_bats = ab
    player.hits = hits
    save_lineup(lineup)
    print(f"{player.full_name} was updated.\n")

def main():
    ui.display_title()
    ui.display_dates()
    ui.display_menu()
    
    lineup = load_lineup()
    
    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            ui.display_menu()
            continue
            
        if option == 1:
            ui.display_lineup(lineup)
        elif option == 2:
            add_player(lineup)
        elif option == 3:
            remove_player(lineup)
        elif option == 4:
            move_player(lineup)
        elif option == 5:
            edit_position(lineup)
        elif option == 6:
            edit_stats(lineup)
        elif option == 7:
            print("Bye!")
            break
        else:
            print("Not a valid menu option. Please try again.\n")
            ui.display_menu()

if __name__ == "__main__":
    main()