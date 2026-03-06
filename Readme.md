#  Baseball Team Manager

A command-line application to manage a baseball team's batting lineup, built in Python.

##  Features

- Display the current lineup with batting averages
- Add, remove, and reorder players
- Edit player positions and statistics
- Persistent storage via CSV file

##  How to Run

### Requirements
- Python 3.8 or higher
- No external dependencies required

### Steps
```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Run the program
python main.py
```

##  Project Structure
```
├── main.py        # Entry point; coordinates all layers
├── ui.py          # Presentation layer (input/output only)
├── objects.py     # Business layer (Player, Lineup classes)
├── db.py          # Data layer (CSV read/write)
└── players.csv    # Persistent player data
```

##  Data Format

Players are stored in `players.csv` with the following columns:
```
Full Name, Position, At Bats, Hits
```

Example:
```
Buster Posey,C,4575,1380
```

##  Design Notes

- **Layered architecture**: UI, business logic, and data access are fully separated.
- **OOP design**: `Player` and `Lineup` classes encapsulate all player data and lineup operations.
- **Input validation**: All user inputs are validated with looping prompts and range checks.

##  Valid Positions

`C, 1B, 2B, 3B, SS, LF, CF, RF, P`
