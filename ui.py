import tkinter as tk
from tkinter import messagebox
import db  # Integrates with your database module [cite: 101]

class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, padx=20, pady=20)
        self.parent = parent
        self.parent.title("Player") # [cite: 112]
        self.pack()

        # StringVars to manage entry data and allow easy clearing [cite: 130, 132]
        self.player_id = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.at_bats = tk.StringVar()
        self.hits = tk.StringVar()
        self.batting_avg = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        # Grid layout matching the Assignment 2 visual [cite: 110]
        
        # Player ID row with "Get Player" button
        tk.Label(self, text="Player ID:").grid(column=0, row=0, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.player_id).grid(column=1, row=0, padx=5)
        tk.Button(self, text="Get Player", command=self.get_player).grid(column=2, row=0, padx=5) # [cite: 125, 128]

        # Standard Data Fields [cite: 114-118]
        tk.Label(self, text="First name:").grid(column=0, row=1, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.first_name).grid(column=1, row=1)

        tk.Label(self, text="Last name:").grid(column=0, row=2, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.last_name).grid(column=1, row=2)

        tk.Label(self, text="Position:").grid(column=0, row=3, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.position).grid(column=1, row=3)

        tk.Label(self, text="At bats:").grid(column=0, row=4, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.at_bats).grid(column=1, row=4)

        tk.Label(self, text="Hits:").grid(column=0, row=5, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.hits).grid(column=1, row=5)

        # Batting Average (Calculated/Read-only) [cite: 120]
        tk.Label(self, text="Batting Avg:").grid(column=0, row=6, sticky=tk.E, pady=2)
        tk.Entry(self, width=30, textvariable=self.batting_avg, state="readonly").grid(column=1, row=6)

        # Action Buttons [cite: 121, 122]
        btn_frame = tk.Frame(self)
        btn_frame.grid(column=1, row=7, pady=15, sticky=tk.W)
        
        tk.Button(btn_frame, text="Save Changes", command=self.save_changes).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.cancel_changes).pack(side=tk.LEFT)

    def get_player(self):
        """Fetches player from DB and populates fields [cite: 128, 129]"""
        try:
            p_id = int(self.player_id.get())
            player = db.get_player(p_id) # Needs to return a Player object or tuple
            
            if player:
                # Assuming player index: 0:id, 1:batOrder, 2:fName, 3:lName, 4:pos, 5:ab, 6:hits [cite: 79-91]
                self.first_name.set(player[2])
                self.last_name.set(player[3])
                self.position.set(player[4])
                self.at_bats.set(player[5])
                self.hits.set(player[6])
                
                # Calculate average for display [cite: 120]
                ab = int(player[5])
                h = int(player[6])
                avg = h / ab if ab > 0 else 0.0
                self.batting_avg.set(f"{avg:.3f}")
            else:
                messagebox.showerror("Error", "Player ID not found.") # [cite: 130]
                self.clear_fields()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric Player ID.")

    def save_changes(self):
        """Updates the database with current field values [cite: 131, 132]"""
        try:
            # Validates and sends data to db module [cite: 135]
            db.Update_player(
                self.player_id.get(),
                self.first_name.get(),
                self.last_name.get(),
                self.position.get(),
                int(self.at_bats.get()),
                int(self.hits.get())
            )
            messagebox.showinfo("Success", "Player updated successfully.")
            self.clear_fields() # [cite: 132]
        except Exception as e:
            messagebox.showerror("Database Error", f"Unable to save: {e}")

    def cancel_changes(self):
        """Restores fields to the last saved state [cite: 133, 134]"""
        if self.player_id.get():
            self.get_player() # Refetches from DB to 'restore' data [cite: 134]
        else:
            self.clear_fields()

    def clear_fields(self):
        """Clears all text entry fields [cite: 130, 132]"""
        self.first_name.set("")
        self.last_name.set("")
        self.position.set("")
        self.at_bats.set("")
        self.hits.set("")
        self.batting_avg.set("")

if __name__ == "__main__":
    root = tk.Tk()
    BaseballGUI(root)
    root.mainloop()